def letter_queue(commands):
    queue = []
    for i in commands:
        temp = i.split()
        if temp[0].strip() == 'PUSH':
            queue.append(temp[1].strip())
        elif temp[0].strip() == 'POP':
            queue = queue[1:]
    return ''.join(queue)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z",
                         "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
