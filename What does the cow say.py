import re
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    print text
    words = text.split()
    if len(words) == 1 & len(text) - text.count(' ') == 1:
        words[0] = re.subn('\s+', ' ', text)[0]
    lines = []
    aLine = []
    for i in words:
        if len(i) > 39:
            while len(i) > 39:
                if aLine:
                    lines.append(' '.join(aLine))
                    aLine = []
                lines.append(i[:39])
                i = i[39:]
            if i:
                aLine.append(i)
        elif sum(map(len, aLine)) + len(aLine) + len(i) <= 39:
            aLine.append(i)
        else:
            lines.append(' '.join(aLine))
            aLine = []
            aLine.append(i)
    else:
        if aLine:
            lines.append(' '.join(aLine))
            aLine = []
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
