def digit_stack(commands):
    stack = []
    sum_of_commands = 0
    for i in commands:
        cmd = i.split()
        if cmd[0] == 'PUSH':
            stack.append(int(cmd[1]))
        elif cmd[0] == 'POP':
            try:
                tmp = stack.pop()
            except IndexError:
                tmp = 0
            sum_of_commands += tmp
        elif cmd[0] == 'PEEK':
            try:
                tmp = stack[-1]
            except IndexError:
                tmp = 0
            sum_of_commands += tmp
    return sum_of_commands


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert (
        digit_stack(
            [
                "PUSH 3",
                "POP",
                "POP",
                "PUSH 4",
                "PEEK",
                "PUSH 9",
                "PUSH 0",
                "PEEK",
                "POP",
                "PUSH 1",
                "PEEK",
            ]
        )
        == 8
    ), "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
