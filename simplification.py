import re
import functools
import operator


class Polynomial:

    def __init__(self, val):
        if isinstance(val, list):
            self.plist = val

    def __add__(self, other):
        if len(self.plist) > len(other.plist):
            new = [i for i in self.plist]
            for i in range(len(other.plist)):
                new[i] += other.plist[i]
        else:
            new = [i for i in other.plist]
            for i in range(len(self.plist)):
                new[i] += self.plist[i]
        return Polynomial(new)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return -Polynomial.__sub__(other)

    def __mul__(self, other):
        result = []
        for i in range(len(other.plist)):
            result.append(
                Polynomial([0] * i + [j * other.plist[i] for j in self.plist]))
        return functools.reduce(operator.add, result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return Polynomial([-1]) * self

    def __repr__(self):
        result = []
        for i in range(len(self.plist)):
            if i == 0:
                result.insert(0, str(self.plist[i]))
            else:
                if self.plist[i] == 0:
                    continue
                else:
                    if self.plist[i] == 1:
                        base_str = 'x'
                    else:
                        base_str = str(self.plist[i]) + '*x'
                    if i == 1:
                        result.insert(0, base_str)
                    else:
                        result.insert(0, base_str + '**' + str(i))
        for i in range(1, len(result)):
            if result[i][0] != '-':
                result[i] = '+' + result[i]

        if result[-1] == '+0' and len(result) > 1:
            result.pop()
        return ''.join(result)


def tokenise(expr):
    symbols = list(expr)
    # merge numbers
    changed = True
    while changed:
        changed = False
        for i in range(len(symbols) - 1):
            try:
                int(symbols[i])
                int(symbols[i + 1])
                symbols = symbols[
                    :i] + [symbols[i] + symbols[i + 1]] + symbols[i + 2:]
                changed = True
                break
            except ValueError:
                pass

    # convert numbers and x
    for i in range(len(symbols)):
        try:
            int(symbols[i])
            symbols[i] = Polynomial([int(symbols[i])])
        except ValueError:
            if symbols[i] == 'x':
                symbols[i] = Polynomial([0, 1])
    # convert neg values
    while '-' in symbols:
        index = symbols.index('-')
        if index == 0 or symbols[index - 1] == '(':
            symbols = symbols[:index] + \
                [-symbols[index + 1]] + symbols[index + 2:]
        else:
            symbols = symbols[
                :index] + ['+', -symbols[index + 1]] + symbols[index + 2:]
    return symbols


def calc(tokens):
    print('input', tokens)
    while len(tokens) > 1:
        # find )
        if ')' in tokens:
            right_bracket = tokens.index(')')
            sub_tokens = tokens[:right_bracket]
            sub_tokens.reverse()
            left_bracket = len(sub_tokens) - sub_tokens.index('(') - 1
            tokens = calc(
                tokens[left_bracket + 1:right_bracket]) + tokens[right_bracket + 1:]
        elif '*' in tokens:
            index = tokens.index('*')
            tokens = tokens[:index-1] + [tokens[index-1]*tokens[index+11]] + tokens[index+2:]
        else:
            index = tokens.index('+')
            tokens = tokens[:index-1] + [tokens[index-1]+tokens[index+1]] + tokens[index+2:]
        print(tokens)
        input()
    return tokens


def simplify(expr):
    tokens = tokenise(expr)
    print(calc(tokens))


if __name__ == "__main__":  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"
