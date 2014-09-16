def checkio(data):
    # replace this for solution
    left_stack = []
    for i in data:
        if i == '(' or i == '[' or i == '{':
            left_stack.append(i)
        elif i == ")":
            if len(left_stack) == 0 or left_stack[-1] != '(':
                return False
            else:
                left_stack.pop()
        elif i == ']':
            if len(left_stack) == 0 or left_stack[-1] != '[':
                return False
            else:
                left_stack.pop()
        elif i == '}':
            if len(left_stack) == 0 or left_stack[-1] != '{':
                return False
            else:
                left_stack.pop()
    if len(left_stack) == 0:
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
