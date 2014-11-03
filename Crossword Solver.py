#!/usr/bin/python
#
# Copyright (c) 2005-2014 - Gustavo Niemeyer <gustavo@niemeyer.net>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import copy

__all__ = ["Problem", "Variable", "Domain", "Unassigned",
           "Solver", "BacktrackingSolver", "Constraint", "FunctionConstraint",
           "AllDifferentConstraint", "AllEqualConstraint", "MaxSumConstraint",
           "ExactSumConstraint", "MinSumConstraint", "InSetConstraint",
           "NotInSetConstraint", "SomeInSetConstraint",
           "SomeNotInSetConstraint"]


class Problem(object):

    def __init__(self):
        self._solver = BacktrackingSolver()
        self._constraints = []
        self._variables = {}

    def reset(self):
        del self._constraints[:]
        self._variables.clear()

    def addVariable(self, variable, domain):
        if variable in self._variables:
            raise ValueError, "Tried to insert duplicated variable %s" % \
                              repr(variable)
        if type(domain) in (list, tuple):
            domain = Domain(domain)
        elif isinstance(domain, Domain):
            domain = copy.copy(domain)
        else:
            raise TypeError, "Domains must be instances of subclasses of "\
                             "the Domain class"
        if not domain:
            raise ValueError, "Domain is empty"
        self._variables[variable] = domain

    def addVariables(self, variables, domain):
        for variable in variables:
            self.addVariable(variable, domain)

    def addConstraint(self, constraint, variables=None):
        if not isinstance(constraint, Constraint):
            if callable(constraint):
                constraint = FunctionConstraint(constraint)
            else:
                raise ValueError, "Constraints must be instances of "\
                                  "subclasses of the Constraint class"
        self._constraints.append((constraint, variables))

    def getSolution(self):
        domains, constraints, vconstraints = self._getArgs()
        if not domains:
            return None
        return self._solver.getSolution(domains, constraints, vconstraints)

    def getSolutions(self):
        domains, constraints, vconstraints = self._getArgs()
        if not domains:
            return []
        return self._solver.getSolutions(domains, constraints, vconstraints)

    def getSolutionIter(self):
        domains, constraints, vconstraints = self._getArgs()
        if not domains:
            return iter(())
        return self._solver.getSolutionIter(domains, constraints,
                                            vconstraints)

    def _getArgs(self):
        domains = self._variables.copy()
        allvariables = domains.keys()
        constraints = []
        for constraint, variables in self._constraints:
            if not variables:
                variables = allvariables
            constraints.append((constraint, variables))
        vconstraints = {}
        for variable in domains:
            vconstraints[variable] = []
        for constraint, variables in constraints:
            for variable in variables:
                vconstraints[variable].append((constraint, variables))
        for constraint, variables in constraints[:]:
            constraint.preProcess(variables, domains,
                                  constraints, vconstraints)
        for domain in domains.values():
            domain.resetState()
            if not domain:
                return None, None, None
        return domains, constraints, vconstraints

# ----------------------------------------------------------------------
# Solvers
# ----------------------------------------------------------------------


class Solver(object):

    def getSolution(self, domains, constraints, vconstraints):
        raise NotImplementedError, \
            "%s is an abstract class" % self.__class__.__name__

    def getSolutions(self, domains, constraints, vconstraints):
        raise NotImplementedError, \
            "%s provides only a single solution" % self.__class__.__name__

    def getSolutionIter(self, domains, constraints, vconstraints):
        raise NotImplementedError, \
            "%s doesn't provide iteration" % self.__class__.__name__


class BacktrackingSolver(Solver):

    def __init__(self, forwardcheck=True):
        self._forwardcheck = forwardcheck

    def getSolutionIter(self, domains, constraints, vconstraints):
        forwardcheck = self._forwardcheck
        assignments = {}

        queue = []

        while True:

            # Mix the Degree and Minimum Remaing Values (MRV) heuristics
            lst = [(-len(vconstraints[variable]),
                    len(domains[variable]), variable) for variable in domains]
            lst.sort()
            for item in lst:
                if item[-1] not in assignments:
                    # Found unassigned variable
                    variable = item[-1]
                    values = domains[variable][:]
                    if forwardcheck:
                        pushdomains = [domains[x] for x in domains
                                       if x not in assignments and
                                       x != variable]
                    else:
                        pushdomains = None
                    break
            else:
                # No unassigned variables. We've got a solution. Go back
                # to last variable, if there's one.
                yield assignments.copy()
                if not queue:
                    return
                variable, values, pushdomains = queue.pop()
                if pushdomains:
                    for domain in pushdomains:
                        domain.popState()

            while True:
                # We have a variable. Do we have any values left?
                if not values:
                    # No. Go back to last variable, if there's one.
                    del assignments[variable]
                    while queue:
                        variable, values, pushdomains = queue.pop()
                        if pushdomains:
                            for domain in pushdomains:
                                domain.popState()
                        if values:
                            break
                        del assignments[variable]
                    else:
                        return

                # Got a value. Check it.
                assignments[variable] = values.pop()

                if pushdomains:
                    for domain in pushdomains:
                        domain.pushState()

                for constraint, variables in vconstraints[variable]:
                    if not constraint(variables, domains, assignments,
                                      pushdomains):
                        # Value is not good.
                        break
                else:
                    break

                if pushdomains:
                    for domain in pushdomains:
                        domain.popState()

            # Push state before looking for next variable.
            queue.append((variable, values, pushdomains))

        raise RuntimeError, "Can't happen"

    def getSolution(self, domains, constraints, vconstraints):
        iter = self.getSolutionIter(domains, constraints, vconstraints)
        try:
            return iter.next()
        except StopIteration:
            return None

    def getSolutions(self, domains, constraints, vconstraints):
        return list(self.getSolutionIter(domains, constraints, vconstraints))


# ----------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------
class Variable(object):

    def __init__(self, name):

        self.name = name

    def __repr__(self):
        return self.name

Unassigned = Variable("Unassigned")

# ----------------------------------------------------------------------
# Domains
# ----------------------------------------------------------------------


class Domain(list):

    def __init__(self, set):

        list.__init__(self, set)
        self._hidden = []
        self._states = []

    def resetState(self):

        self.extend(self._hidden)
        del self._hidden[:]
        del self._states[:]

    def pushState(self):

        self._states.append(len(self))

    def popState(self):

        diff = self._states.pop() - len(self)
        if diff:
            self.extend(self._hidden[-diff:])
            del self._hidden[-diff:]

    def hideValue(self, value):

        list.remove(self, value)
        self._hidden.append(value)

# ----------------------------------------------------------------------
# Constraints
# ----------------------------------------------------------------------


class Constraint(object):

    def __call__(self, variables, domains, assignments, forwardcheck=False):

        return True

    def preProcess(self, variables, domains, constraints, vconstraints):

        if len(variables) == 1:
            variable = variables[0]
            domain = domains[variable]
            for value in domain[:]:
                if not self(variables, domains, {variable: value}):
                    domain.remove(value)
            constraints.remove((self, variables))
            vconstraints[variable].remove((self, variables))

    def forwardCheck(self, variables, domains, assignments,
                     _unassigned=Unassigned):

        unassignedvariable = _unassigned
        for variable in variables:
            if variable not in assignments:
                if unassignedvariable is _unassigned:
                    unassignedvariable = variable
                else:
                    break
        else:
            if unassignedvariable is not _unassigned:
                # Remove from the unassigned variable domain's all
                # values which break our variable's constraints.
                domain = domains[unassignedvariable]
                if domain:
                    for value in domain[:]:
                        assignments[unassignedvariable] = value
                        if not self(variables, domains, assignments):
                            domain.hideValue(value)
                    del assignments[unassignedvariable]
                if not domain:
                    return False
        return True


class FunctionConstraint(Constraint):

    def __init__(self, func, assigned=True):

        self._func = func
        self._assigned = assigned

    def __call__(self, variables, domains, assignments, forwardcheck=False,
                 _unassigned=Unassigned):
        parms = [assignments.get(x, _unassigned) for x in variables]
        missing = parms.count(_unassigned)
        if missing:
            return ((self._assigned or self._func(*parms)) and
                    (not forwardcheck or missing != 1 or
                     self.forwardCheck(variables, domains, assignments)))
        return self._func(*parms)


class AllDifferentConstraint(Constraint):

    def __call__(self, variables, domains, assignments, forwardcheck=False,
                 _unassigned=Unassigned):
        seen = {}
        for variable in variables:
            value = assignments.get(variable, _unassigned)
            if value is not _unassigned:
                if value in seen:
                    return False
                seen[value] = True
        if forwardcheck:
            for variable in variables:
                if variable not in assignments:
                    domain = domains[variable]
                    for value in seen:
                        if value in domain:
                            domain.hideValue(value)
                            if not domain:
                                return False
        return True


class AllEqualConstraint(Constraint):

    def __call__(self, variables, domains, assignments, forwardcheck=False,
                 _unassigned=Unassigned):
        singlevalue = _unassigned
        for variable in variables:
            value = assignments.get(variable, _unassigned)
            if singlevalue is _unassigned:
                singlevalue = value
            elif value is not _unassigned and value != singlevalue:
                return False
        if forwardcheck and singlevalue is not _unassigned:
            for variable in variables:
                if variable not in assignments:
                    domain = domains[variable]
                    if singlevalue not in domain:
                        return False
                    for value in domain[:]:
                        if value != singlevalue:
                            domain.hideValue(value)
        return True


class MaxSumConstraint(Constraint):

    def __init__(self, maxsum, multipliers=None):
        self._maxsum = maxsum
        self._multipliers = multipliers

    def preProcess(self, variables, domains, constraints, vconstraints):
        Constraint.preProcess(self, variables, domains,
                              constraints, vconstraints)
        multipliers = self._multipliers
        maxsum = self._maxsum
        if multipliers:
            for variable, multiplier in zip(variables, multipliers):
                domain = domains[variable]
                for value in domain[:]:
                    if value * multiplier > maxsum:
                        domain.remove(value)
        else:
            for variable in variables:
                domain = domains[variable]
                for value in domain[:]:
                    if value > maxsum:
                        domain.remove(value)

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        multipliers = self._multipliers
        maxsum = self._maxsum
        sum = 0
        if multipliers:
            for variable, multiplier in zip(variables, multipliers):
                if variable in assignments:
                    sum += assignments[variable] * multiplier
            if type(sum) is float:
                sum = round(sum, 10)
            if sum > maxsum:
                return False
            if forwardcheck:
                for variable, multiplier in zip(variables, multipliers):
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if sum + value * multiplier > maxsum:
                                domain.hideValue(value)
                        if not domain:
                            return False
        else:
            for variable in variables:
                if variable in assignments:
                    sum += assignments[variable]
            if type(sum) is float:
                sum = round(sum, 10)
            if sum > maxsum:
                return False
            if forwardcheck:
                for variable in variables:
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if sum + value > maxsum:
                                domain.hideValue(value)
                        if not domain:
                            return False
        return True


class ExactSumConstraint(Constraint):

    def __init__(self, exactsum, multipliers=None):
        self._exactsum = exactsum
        self._multipliers = multipliers

    def preProcess(self, variables, domains, constraints, vconstraints):
        Constraint.preProcess(self, variables, domains,
                              constraints, vconstraints)
        multipliers = self._multipliers
        exactsum = self._exactsum
        if multipliers:
            for variable, multiplier in zip(variables, multipliers):
                domain = domains[variable]
                for value in domain[:]:
                    if value * multiplier > exactsum:
                        domain.remove(value)
        else:
            for variable in variables:
                domain = domains[variable]
                for value in domain[:]:
                    if value > exactsum:
                        domain.remove(value)

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        multipliers = self._multipliers
        exactsum = self._exactsum
        sum = 0
        missing = False
        if multipliers:
            for variable, multiplier in zip(variables, multipliers):
                if variable in assignments:
                    sum += assignments[variable] * multiplier
                else:
                    missing = True
            if type(sum) is float:
                sum = round(sum, 10)
            if sum > exactsum:
                return False
            if forwardcheck and missing:
                for variable, multiplier in zip(variables, multipliers):
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if sum + value * multiplier > exactsum:
                                domain.hideValue(value)
                        if not domain:
                            return False
        else:
            for variable in variables:
                if variable in assignments:
                    sum += assignments[variable]
                else:
                    missing = True
            if type(sum) is float:
                sum = round(sum, 10)
            if sum > exactsum:
                return False
            if forwardcheck and missing:
                for variable in variables:
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if sum + value > exactsum:
                                domain.hideValue(value)
                        if not domain:
                            return False
        if missing:
            return sum <= exactsum
        else:
            return sum == exactsum


class MinSumConstraint(Constraint):

    def __init__(self, minsum, multipliers=None):

        self._minsum = minsum
        self._multipliers = multipliers

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        for variable in variables:
            if variable not in assignments:
                return True
        else:
            multipliers = self._multipliers
            minsum = self._minsum
            sum = 0
            if multipliers:
                for variable, multiplier in zip(variables, multipliers):
                    sum += assignments[variable] * multiplier
            else:
                for variable in variables:
                    sum += assignments[variable]
            if type(sum) is float:
                sum = round(sum, 10)
            return sum >= minsum


class InSetConstraint(Constraint):

    def __init__(self, set):

        self._set = set

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        # preProcess() will remove it.
        raise RuntimeError, "Can't happen"

    def preProcess(self, variables, domains, constraints, vconstraints):
        set = self._set
        for variable in variables:
            domain = domains[variable]
            for value in domain[:]:
                if value not in set:
                    domain.remove(value)
            vconstraints[variable].remove((self, variables))
        constraints.remove((self, variables))


class NotInSetConstraint(Constraint):

    def __init__(self, set):

        self._set = set

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        # preProcess() will remove it.
        raise RuntimeError, "Can't happen"

    def preProcess(self, variables, domains, constraints, vconstraints):
        set = self._set
        for variable in variables:
            domain = domains[variable]
            for value in domain[:]:
                if value in set:
                    domain.remove(value)
            vconstraints[variable].remove((self, variables))
        constraints.remove((self, variables))


class SomeInSetConstraint(Constraint):

    def __init__(self, set, n=1, exact=False):
        self._set = set
        self._n = n
        self._exact = exact

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        set = self._set
        missing = 0
        found = 0
        for variable in variables:
            if variable in assignments:
                found += assignments[variable] in set
            else:
                missing += 1
        if missing:
            if self._exact:
                if not (found <= self._n <= missing + found):
                    return False
            else:
                if self._n > missing + found:
                    return False
            if forwardcheck and self._n - found == missing:
                # All unassigned variables must be assigned to
                # values in the set.
                for variable in variables:
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if value not in set:
                                domain.hideValue(value)
                        if not domain:
                            return False
        else:
            if self._exact:
                if found != self._n:
                    return False
            else:
                if found < self._n:
                    return False
        return True


class SomeNotInSetConstraint(Constraint):

    def __init__(self, set, n=1, exact=False):
        self._set = set
        self._n = n
        self._exact = exact

    def __call__(self, variables, domains, assignments, forwardcheck=False):
        set = self._set
        missing = 0
        found = 0
        for variable in variables:
            if variable in assignments:
                found += assignments[variable] not in set
            else:
                missing += 1
        if missing:
            if self._exact:
                if not (found <= self._n <= missing + found):
                    return False
            else:
                if self._n > missing + found:
                    return False
            if forwardcheck and self._n - found == missing:
                # All unassigned variables must be assigned to
                # values not in the set.
                for variable in variables:
                    if variable not in assignments:
                        domain = domains[variable]
                        for value in domain[:]:
                            if value in set:
                                domain.hideValue(value)
                        if not domain:
                            return False
        else:
            if self._exact:
                if found != self._n:
                    return False
            else:
                if found < self._n:
                    return False
        return True


def solver(crossword, words):
    CrosswordProblem = Problem()
    EmptySlots = []
    for row in range(len(crossword)):
        for col in range(len(crossword[row])):
            if crossword[row][col] == '.':
                EmptySlots.append((row, col))

    # group empty slots
    EmptySlots = [[i] for i in EmptySlots]
    Changed = True
    WordsInRows = copy.deepcopy(EmptySlots)
    while Changed:
        Changed = False
        for i in range(len(WordsInRows)-1):
            if (WordsInRows[i][-1][0] == WordsInRows[i+1][0][0]
                    and WordsInRows[i][-1][1] - WordsInRows[i+1][0][1] == -1):
                WordsInRows[i] += WordsInRows[i+1]
                WordsInRows.remove(WordsInRows[i+1])
                Changed = True
                break

    WordsInCols = copy.deepcopy(EmptySlots)
    WordsInCols = sorted(WordsInCols, key=lambda x: x[0][1])
    Changed = True
    while Changed:
        Changed = False
        for i in range(len(WordsInCols)-1):
            if (WordsInCols[i][-1][1] == WordsInCols[i+1][0][1]
                    and WordsInCols[i][-1][0] - WordsInCols[i+1][0][0] == -1):
                WordsInCols[i] += WordsInCols[i+1]
                WordsInCols.remove(WordsInCols[i+1])
                Changed = True
                break
    WordSlots = [i for i in WordsInRows + WordsInCols if len(i) > 1]

    for i in WordSlots:
        CrosswordProblem.addVariable(WordSlots.index(i),
                                     filter(lambda x: len(x) == len(i),
                                            words))
    CrosswordProblem.addConstraint(AllDifferentConstraint())

    # constraint rules for all cross points
    for i in range(len(WordSlots)-1):
        for j in range(i+1, len(WordSlots)):
            CrossPosition = [k for k in WordSlots[i] if k in WordSlots[j]]
            if CrossPosition:
                CrossPosition = CrossPosition[0]
                p0 = WordSlots[i].index(CrossPosition)
                p1 = WordSlots[j].index(CrossPosition)
                CrosswordProblem.addConstraint(lambda x, y, p0=p0, p1=p1:
                                               x[p0] == y[p1],
                                               (i, j))

    solution = CrosswordProblem.getSolution()
    FilledCrossword = [list(i) for i in crossword]
    for i in solution:
        for j, k in enumerate(solution[i]):
            FilledCrossword[WordSlots[i][j][0]][WordSlots[i][j][1]] = solution[i][j]
    FilledCrossword = [''.join(i) for i in FilledCrossword]
    return FilledCrossword



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for
    #auto-testing
    import string

    ERROR_TYPE = (False, "The result must be a list/tuple of strings")
    ERROR_SIZE = (False, "The result must have the same size as input data")
    ERROR_TEMPLATE = (False, "Your result is not look like the original crossword")
    ERROR_UNFILLED = (False, "I see the empty cell in your result")
    ERROR_TYPE_CELL = (False, "Cells should contains lowercase ascii letters or 'X'")
    F_ERROR_REPEATED = lambda w: (False, "Found repeated words '{}'".format(w))
    F_ERROR_UNKNOWN = lambda w: (False, "The word '{}' is not from the dictionary".format(w))
    WORDS = ['act', 'age', 'air', 'arm', 'art', 'ask', 'bad', 'bag', 'bar', 'bat', 'bed', 'bet', 'bid', 'big', 'bit', 'box', 'boy', 'bug', 'bus', 'buy', 'can', 'cap', 'car', 'cat', 'cow', 'cry', 'cup', 'cut', 'dad', 'day', 'dig', 'dog', 'dot', 'due', 'ear', 'eat', 'egg', 'end', 'eye', 'fan', 'fat', 'fee', 'few', 'fix', 'fly', 'fun', 'gap', 'gas', 'god', 'guy', 'hat', 'hit', 'ice', 'job', 'key', 'kid', 'lab', 'law', 'lay', 'leg', 'let', 'lie', 'lip', 'log', 'low', 'man', 'map', 'mix', 'mom', 'mud', 'net', 'oil', 'one', 'pay', 'pen', 'pie', 'pin', 'pop', 'pot', 'put', 'raw', 'red', 'rip', 'row', 'rub', 'run', 'sad', 'sea', 'set', 'sex', 'she', 'sir', 'sky', 'son', 'sun', 'tap', 'tax', 'tea', 'tie', 'tip', 'toe', 'top', 'try', 'two', 'use', 'war', 'way', 'web', 'win', 'you', 'area', 'army', 'baby', 'back', 'bake', 'ball', 'band', 'bank', 'base', 'bath', 'bear', 'beat', 'beer', 'bell', 'belt', 'bend', 'bike', 'bill', 'bird', 'bite', 'blow', 'blue', 'boat', 'body', 'bone', 'book', 'boot', 'boss', 'bowl', 'burn', 'cake', 'call', 'calm', 'camp', 'card', 'care', 'case', 'cash', 'cell', 'chip', 'city', 'club', 'clue', 'coat', 'code', 'cold', 'cook', 'copy', 'cost', 'crew', 'dare', 'dark', 'data', 'date', 'dead', 'deal', 'dear', 'debt', 'deep', 'desk', 'diet', 'dirt', 'dish', 'disk', 'door', 'drag', 'draw', 'drop', 'dump', 'dust', 'duty', 'ease', 'east', 'edge', 'exam', 'exit', 'face', 'fact', 'fall', 'farm', 'fear', 'feed', 'feel', 'file', 'fill', 'film', 'fire', 'fish', 'flow', 'fold', 'food', 'foot', 'form', 'fuel', 'gain', 'game', 'gate', 'gear', 'gene', 'gift', 'girl', 'give', 'glad', 'goal', 'gold', 'golf', 'good', 'grab', 'hair', 'half', 'hall', 'hand', 'hang', 'harm', 'hate', 'head', 'heat', 'hell', 'help', 'hide', 'high', 'hire', 'hold', 'hole', 'home', 'hook', 'hope', 'host', 'hour', 'hunt', 'hurt', 'idea', 'iron', 'item', 'join', 'joke', 'jump', 'jury', 'keep', 'kick', 'kill', 'kind', 'king', 'kiss', 'knee', 'lack', 'lady', 'lake', 'land', 'lead', 'life', 'lift', 'line', 'link', 'list', 'load', 'loan', 'lock', 'long', 'look', 'loss', 'love', 'luck', 'mail', 'main', 'make', 'male', 'mall', 'many', 'mark', 'mate', 'math', 'meal', 'meat', 'meet', 'menu', 'mess', 'milk', 'mind', 'mine', 'miss', 'mode', 'mood', 'most', 'move', 'nail', 'name', 'neat', 'neck', 'news', 'nose', 'note', 'oven', 'pace', 'pack', 'page', 'pain', 'pair', 'park', 'part', 'pass', 'past', 'path', 'peak', 'pick', 'pipe', 'plan', 'play', 'poem', 'poet', 'pool', 'post', 'pull', 'push', 'quit', 'race', 'rain', 'rate', 'read', 'rent', 'rest', 'rice', 'rich', 'ride', 'ring', 'rise', 'risk', 'road', 'rock', 'role', 'roll', 'roof', 'room', 'rope', 'ruin', 'rule', 'rush', 'safe', 'sail', 'sale', 'salt', 'sand', 'save', 'seat', 'self', 'sell', 'ship', 'shoe', 'shop', 'shot', 'show', 'sick', 'side', 'sign', 'sing', 'sink', 'site', 'size', 'skin', 'slip', 'snow', 'sock', 'soft', 'soil', 'song', 'sort', 'soup', 'spot', 'star', 'stay', 'step', 'stop', 'suck', 'suit', 'swim', 'tale', 'talk', 'tank', 'task', 'team', 'tear', 'tell', 'term', 'test', 'text', 'till', 'time', 'tone', 'tool', 'tour', 'town', 'tree', 'trip', 'tune', 'turn', 'type', 'unit', 'user', 'vast', 'verb', 'verb', 'verb', 'view', 'wait', 'wake', 'walk', 'wall', 'wash', 'wave', 'wear', 'week', 'west', 'wife', 'will', 'wind', 'wine', 'wing', 'wish', 'wood', 'word', 'work', 'wrap', 'yard', 'year', 'zone', 'abuse', 'actor', 'adult', 'agent', 'alarm', 'anger', 'angle', 'apple', 'aside', 'award', 'basis', 'beach', 'being', 'bench', 'birth', 'black', 'blame', 'blank', 'blind', 'block', 'blood', 'board', 'bonus', 'brain', 'brave', 'bread', 'break', 'brick', 'brief', 'broad', 'brown', 'brush', 'buddy', 'bunch', 'buyer', 'cable', 'candy', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'check', 'cheek', 'chest', 'child', 'claim', 'class', 'clerk', 'click', 'clock', 'cloud', 'coach', 'coast', 'count', 'court', 'cover', 'crack', 'craft', 'crash', 'crazy', 'cream', 'cross', 'curve', 'cycle', 'dance', 'death', 'delay', 'depth', 'devil', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'drunk', 'earth', 'entry', 'equal', 'error', 'essay', 'event', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'front', 'fruit', 'funny', 'glass', 'glove', 'grade', 'grand', 'grass', 'great', 'green', 'group', 'guard', 'guess', 'guest', 'guide', 'habit', 'heart', 'heavy', 'hello', 'honey', 'horse', 'hotel', 'house', 'human', 'hurry', 'ideal', 'image', 'issue', 'joint', 'judge', 'juice', 'knife', 'laugh', 'layer', 'leave', 'level', 'light', 'limit', 'local', 'lunch', 'major', 'march', 'match', 'maybe', 'media', 'metal', 'might', 'minor', 'model', 'money', 'month', 'motor', 'mouse', 'mouth', 'movie', 'music', 'nasty', 'nerve', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'paint', 'panic', 'paper', 'party', 'pause', 'peace', 'phase', 'phone', 'photo', 'piano', 'piece', 'pitch', 'pizza', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'print', 'prior', 'prize', 'proof', 'punch', 'queen', 'quiet', 'quote', 'radio', 'raise', 'range', 'ratio', 'reach', 'reply', 'river', 'rough', 'round', 'royal', 'salad', 'scale', 'scene', 'score', 'screw', 'sense', 'serve', 'shake', 'shame', 'shape', 'share', 'shift', 'shine', 'shirt', 'shock', 'shoot', 'silly', 'skill', 'skirt', 'sleep', 'slice', 'slide', 'smile', 'smoke', 'solid', 'sound', 'south', 'space', 'spare', 'speed', 'spell', 'spend', 'spite', 'split', 'sport', 'spray', 'staff', 'stage', 'stand', 'start', 'state', 'steak', 'steal', 'stick', 'still', 'stock', 'store', 'storm', 'story', 'strip', 'study', 'stuff', 'style', 'sugar', 'sweet', 'swing', 'table', 'taste', 'teach', 'theme', 'thing', 'title', 'today', 'tooth', 'topic', 'total', 'touch', 'tough', 'towel', 'tower', 'track', 'trade', 'train', 'trash', 'treat', 'trick', 'truck', 'trust', 'truth', 'twist', 'uncle', 'union', 'upper', 'usual', 'value', 'video', 'virus', 'visit', 'voice', 'watch', 'water', 'weird', 'wheel', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'worth', 'young', 'youth', 'abroad', 'access', 'action', 'active', 'advice', 'affair', 'affect', 'agency', 'amount', 'animal', 'annual', 'answer', 'appeal', 'aspect', 'assist', 'attack', 'author', 'basket', 'battle', 'beyond', 'bitter', 'border', 'boring', 'bother', 'bottle', 'bottom', 'branch', 'breast', 'breath', 'bridge', 'budget', 'button', 'camera', 'cancel', 'cancer', 'candle', 'career', 'carpet', 'chance', 'change', 'charge', 'choice', 'church', 'client', 'closet', 'coffee', 'collar', 'common', 'cookie', 'corner', 'county', 'couple', 'course', 'cousin', 'credit', 'damage', 'dealer', 'debate', 'degree', 'demand', 'design', 'desire', 'detail', 'device', 'dinner', 'divide', 'doctor', 'double', 'drawer', 'driver', 'editor', 'effect', 'effort', 'employ', 'energy', 'engine', 'escape', 'estate', 'excuse', 'expert', 'extent', 'factor', 'family', 'farmer', 'father', 'female', 'figure', 'finger', 'finish', 'flight', 'flower', 'formal', 'friend', 'future', 'garage', 'garden', 'gather', 'ground', 'growth', 'guitar', 'handle', 'health', 'height', 'horror', 'impact', 'income', 'injury', 'insect', 'inside', 'invite', 'island', 'jacket', 'junior', 'ladder', 'lawyer', 'leader', 'league', 'length', 'lesson', 'letter', 'listen', 'living', 'manner', 'market', 'master', 'matter', 'medium', 'member', 'memory', 'method', 'middle', 'minute', 'mirror', 'mobile', 'moment', 'mother', 'muscle', 'nation', 'native', 'nature', 'nobody', 'normal', 'notice', 'number', 'object', 'office', 'option', 'orange', 'parent', 'people', 'period', 'permit', 'person', 'phrase', 'player', 'plenty', 'poetry', 'police', 'policy', 'potato', 'priest', 'profit', 'prompt', 'public', 'purple', 'reason', 'recipe', 'record', 'refuse', 'region', 'regret', 'relief', 'remote', 'remove', 'repair', 'repeat', 'report', 'resist', 'resort', 'result', 'return', 'reveal', 'review', 'reward', 'safety', 'salary', 'sample', 'scheme', 'school', 'screen', 'script', 'search', 'season', 'second', 'secret', 'sector', 'senior', 'series', 'shower', 'signal', 'silver', 'simple', 'singer', 'single', 'sister', 'source', 'speech', 'spirit', 'spread', 'spring', 'square', 'stable', 'status', 'strain', 'street', 'stress', 'strike', 'string', 'stroke', 'studio', 'stupid', 'summer', 'survey', 'switch', 'system', 'tackle', 'target', 'tennis', 'thanks', 'theory', 'throat', 'ticket', 'tongue', 'travel', 'unique', 'visual', 'volume', 'wealth', 'weight', 'window', 'winner', 'winter', 'wonder', 'worker', 'writer', 'yellow', 'ability', 'account', 'address', 'advance', 'airline', 'airport', 'alcohol', 'analyst', 'anxiety', 'anybody', 'arrival', 'article', 'article', 'attempt', 'average', 'balance', 'bedroom', 'benefit', 'bicycle', 'brother', 'cabinet', 'capital', 'channel', 'chapter', 'charity', 'chicken', 'classic', 'climate', 'clothes', 'college', 'combine', 'comfort', 'command', 'comment', 'company', 'complex', 'concept', 'concern', 'concert', 'consist', 'contact', 'contest', 'context', 'control', 'convert', 'counter', 'country', 'courage', 'culture', 'current', 'deposit', 'diamond', 'disease', 'display', 'drawing', 'economy', 'emotion', 'evening', 'example', 'extreme', 'failure', 'feature', 'feeling', 'finance', 'finding', 'fishing', 'forever', 'fortune', 'freedom', 'funeral', 'garbage', 'general', 'grocery', 'hearing', 'highway', 'history', 'holiday', 'housing', 'husband', 'illegal', 'impress', 'initial', 'kitchen', 'leading', 'leather', 'lecture', 'library', 'machine', 'manager', 'maximum', 'meaning', 'meeting', 'mention', 'message', 'minimum', 'mission', 'mistake', 'mixture', 'monitor', 'morning', 'natural', 'network', 'nothing', 'officer', 'opening', 'opinion', 'outcome', 'outside', 'package', 'parking', 'partner', 'passage', 'passion', 'patient', 'pattern', 'payment', 'penalty', 'pension', 'physics', 'picture', 'plastic', 'present', 'primary', 'private', 'problem', 'process', 'produce', 'product', 'profile', 'program', 'project', 'promise', 'purpose', 'quality', 'quarter', 'reading', 'reality', 'recover', 'regular', 'release', 'request', 'reserve', 'resolve', 'respect', 'respond', 'revenue', 'routine', 'savings', 'science', 'scratch', 'section', 'service', 'session', 'setting', 'shelter', 'society', 'speaker', 'special', 'station', 'stomach', 'storage', 'stretch', 'student', 'subject', 'success', 'support', 'surgery', 'suspect', 'teacher', 'tension', 'thought', 'tonight', 'tourist', 'traffic', 'trainer', 'trouble', 'variety', 'vehicle', 'version', 'village', 'warning', 'weather', 'wedding', 'weekend', 'welcome', 'western', 'whereas', 'witness', 'working', 'writing', 'accident', 'activity', 'addition', 'ambition', 'analysis', 'anything', 'anywhere', 'argument', 'attitude', 'audience', 'baseball', 'bathroom', 'birthday', 'building', 'business', 'calendar', 'campaign', 'category', 'champion', 'chemical', 'computer', 'conflict', 'constant', 'contract', 'creative', 'currency', 'customer', 'database', 'daughter', 'decision', 'delivery', 'designer', 'director', 'disaster', 'discount', 'distance', 'district', 'document', 'election', 'elevator', 'emphasis', 'employee', 'employer', 'engineer', 'entrance', 'estimate', 'evidence', 'exchange', 'exercise', 'external', 'familiar', 'feedback', 'football', 'function', 'guidance', 'homework', 'hospital', 'incident', 'increase', 'industry', 'instance', 'interest', 'internal', 'internet', 'judgment', 'language', 'location', 'magazine', 'marriage', 'material', 'medicine', 'midnight', 'mortgage', 'mountain', 'national', 'negative', 'occasion', 'official', 'opposite', 'ordinary', 'original', 'painting', 'patience', 'personal', 'physical', 'platform', 'pleasure', 'politics', 'position', 'positive', 'possible', 'practice', 'presence', 'pressure', 'priority', 'progress', 'property', 'proposal', 'purchase', 'quantity', 'question', 'reaction', 'register', 'relation', 'relative', 'republic', 'research', 'resident', 'resource', 'response', 'sandwich', 'schedule', 'security', 'sentence', 'shopping', 'shoulder', 'software', 'solution', 'specific', 'standard', 'stranger', 'strategy', 'strength', 'struggle', 'surprise', 'surround', 'swimming', 'sympathy', 'teaching', 'tomorrow', 'training', 'upstairs', 'vacation', 'valuable', 'weakness', 'advantage', 'afternoon', 'agreement', 'apartment', 'assistant', 'associate', 'attention', 'awareness', 'beautiful', 'beginning', 'boyfriend', 'breakfast', 'brilliant', 'candidate', 'challenge', 'character', 'chemistry', 'childhood', 'chocolate', 'cigarette', 'classroom', 'committee', 'community', 'complaint', 'condition', 'confusion', 'criticism', 'departure', 'dependent', 'dimension', 'direction', 'economics', 'education', 'effective', 'emergency', 'equipment', 'extension', 'following', 'guarantee', 'highlight', 'historian', 'implement', 'inflation', 'influence', 'inspector', 'insurance', 'intention', 'interview', 'knowledge', 'landscape', 'marketing', 'necessary', 'newspaper', 'objective', 'operation', 'passenger', 'pollution', 'potential', 'president', 'principle', 'procedure', 'professor', 'promotion', 'reception', 'recording', 'reference', 'secretary', 'selection', 'sensitive', 'signature', 'situation', 'somewhere', 'spiritual', 'statement', 'structure', 'substance', 'telephone', 'temporary', 'tradition', 'variation', 'vegetable', 'yesterday', 'appearance', 'assignment', 'assistance', 'assumption', 'atmosphere', 'background', 'collection', 'commercial', 'commission', 'comparison', 'conclusion', 'conference', 'confidence', 'connection', 'definition', 'department', 'depression', 'difference', 'difficulty', 'discipline', 'discussion', 'efficiency', 'employment', 'enthusiasm', 'equivalent', 'excitement', 'experience', 'expression', 'foundation', 'friendship', 'girlfriend', 'government', 'importance', 'impression', 'indication', 'individual', 'inevitable', 'initiative', 'inspection', 'investment', 'leadership', 'literature', 'management', 'membership', 'obligation', 'particular', 'percentage', 'perception', 'permission', 'philosophy', 'population', 'possession', 'preference', 'profession', 'protection', 'psychology', 'reflection', 'reputation', 'resolution', 'restaurant', 'revolution', 'specialist', 'suggestion', 'technology', 'television', 'transition', 'university', 'advertising', 'alternative', 'application', 'appointment', 'association', 'celebration', 'combination', 'comfortable', 'competition', 'concentrate', 'consequence', 'description', 'development', 'engineering', 'environment', 'examination', 'explanation', 'grandfather', 'grandmother', 'imagination', 'improvement', 'independent', 'information', 'instruction', 'interaction', 'maintenance', 'measurement', 'negotiation', 'opportunity', 'performance', 'personality', 'perspective', 'possibility', 'preparation', 'recognition', 'replacement', 'requirement', 'supermarket', 'temperature', 'championship', 'construction', 'contribution', 'conversation', 'distribution', 'independence', 'introduction', 'manufacturer', 'organization', 'presentation', 'professional', 'refrigerator', 'relationship', 'satisfaction', 'significance', 'communication', 'consideration', 'entertainment', 'establishment', 'international', 'understanding', 'administration', 'recommendation', 'representative', 'responsibility', 'transportation']

    def find_word(grid, row, col):
        word = ""
        while col < len(grid[row]) and grid[row][col] != "X":
            word += grid[row][col]
            col += 1
        return word

    def checker(func, template):
        result = func(template, WORDS)
        # types check
        if not isinstance(result, (tuple, list)):
            return ERROR_TYPE
        if not all(isinstance(row, (str, unicode)) for row in result):
            return ERROR_TYPE

        # size check
        if (len(result) != len(template) or
                any(len(result[i]) != len(template[i]) for i in range(len(template)))):
            return ERROR_SIZE

        # template, letters and filled check
        for i, row in enumerate(result):
            for j, ch in enumerate(row):
                if ch == "X":
                    if template[i][j] != "X":
                        return ERROR_TEMPLATE
                elif ch == ".":
                    return ERROR_UNFILLED
                elif ch in string.ascii_lowercase:
                    if template[i][j] != ".":
                        return ERROR_TEMPLATE
                else:
                    return ERROR_TYPE_CELL

        # words checking
        used_words = set()
        rotated_result = ["".join(row) for row in zip(*result)]

        words = []
        for k, row in enumerate(template):
            for m, symb in enumerate(row):
                if symb == "X":
                    continue
                if (k == 0 or template[k - 1][m] == "X") and (k < len(template) - 1 and template[k + 1][m] == "."):
                    words.append(find_word(rotated_result, m, k))
                if (m == 0 or template[k][m - 1] == "X") and (m < len(template[k]) - 1 and template[k][m + 1] == "."):
                    words.append(find_word(result, k, m))
        for w in words:
            if w in used_words:
                return F_ERROR_REPEATED(w)
            used_words.add(w)
            if w not in WORDS:
                return F_ERROR_UNKNOWN(w)
        return True, "Great!"

    result, message = checker(solver, [u'.XXX.', u'...X.', u'.X.X.', u'.....'])
    assert result, "1st example. " + message

    result, message = checker(solver, [u'X.XX', u'....', u'X.XX', u'X...', u'XXX.', u'....', u'XXX.'],)
    assert result, "2nd example. " + message

    result, message = checker(solver, [u'...XXXXXX', u'.XXX.X...', u'.....X.XX', u'XXXX.X...',
                                       u'XX...X.XX', u'XX.XXX.X.', u'X......X.', u'XX.X.XXX.', u'XXXX.....'],)
    assert result, "3rd example. " + message

