def checkio(data):
    # replace this for solution
    leftStack = []
    for i in data:
        if i == '(' or i == '[' or i == '{':
            leftStack.append(i)
        elif i == ")":
            if len(leftStack) == 0 or leftStack[-1] != '(':
                return False
            else:
                leftStack.pop()
        elif i == ']':
            if len(leftStack) == 0 or leftStack[-1] != '[':
                return False
            else:
                leftStack.pop()
        elif i == '}':
            if len(leftStack) == 0 or leftStack[-1] != '{':
                return False
            else:
                leftStack.pop()
    if len(leftStack) == 0:
        return True
    else:
        return False

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
