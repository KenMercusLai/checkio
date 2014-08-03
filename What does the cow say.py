import re
from copy import deepcopy
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    # replace multiple space with single space
    newText = re.subn('\s+', ' ', text)[0]
    # split text into elements
    elements = []
    word = ''
    for i in newText:
        if i == ' ':
            if word:
                elements.append(word)
                word = ''
            elements.append(i)
        else:
            word = word + i
    else:
        if word:
            elements.append(word)

    # find if there are words longer than 39, cut it for every 39
    elementsCopy = deepcopy(elements)
    for i, j in enumerate(elements):
        if len(j) > 39:
            print i, j
            tempList = []
            while len(j) > 39:
                tempList.append(j[:39])
                j = j[39:]
            if j:
                tempList.append(j)
            elementsCopy = elementsCopy[:i] + tempList + elementsCopy[i + 1:]
    elements = deepcopy(elementsCopy)

    # arrange elements
    lines = []
    oneLine = ''
    for i in elements:
        if len(oneLine) + len(i) <= 39:
            oneLine = oneLine + i
        else:
            if i == ' ':
                pass
            else:
                if oneLine[-1] == ' ':
                    lines.append(oneLine[:-1])
                else:
                    lines.append(oneLine)
                oneLine = i
    else:
        lines.append(oneLine)

    # let the cow say
    maxLength = max(map(len, lines))
    if len(lines) == 1:
        lines[0] = '< ' + lines[0] + ' >'
    else:
        formatString = '{:<%s}' % maxLength
        for i, j in enumerate(lines):
            if i == 0:
                lines[i] = '/ ' + formatString.format(j) + ' \\'
            else:
                lines[i] = '| ' + formatString.format(j) + ' |'
        else:
            lines[i] = '\\ ' + formatString.format(j) + ' /'
    lines = [' ' + '_' * (maxLength + 2)] + lines + \
        [' ' + '-' * (maxLength + 2)]
    return '\n%s%s' % ('\n'.join(lines), COW)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                               'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
