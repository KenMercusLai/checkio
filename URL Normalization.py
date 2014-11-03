import re


def checkio(url):
    # rule 4
    url = re.sub(':80/', '/', url)
    url = re.sub(':80$', '', url)
    # rule 1
    url = url.lower()
    # rule 2
    while re.search('(%[a-z][a-z])', url):
        url = re.sub('(%[a-z][a-z])',
                     lambda x: x.groups()[0].upper(), url)
    while re.search('(%[a-z]\d)', url):
        url = re.sub('(%[a-z]\d)',
                     lambda x: x.groups()[0].upper(), url)
    while re.search('(%\d[a-z])', url):
        url = re.sub('(%\d[a-z])',
                     lambda x: x.groups()[0].upper(), url)

    # rule 3
    def fun(match):
        char = match.groups()[0]
        if any([True for i in [('41', '5A'), ('61', '7A'), ('30', '39'),
                               ('2D', '2E'), ('5F', '5F'), ('7E', '7E')]
                if i[0] <= char <= i[1]]):
            return chr(int(char, 16))
        else:
            return '%' + char
    url = re.sub('%([\w|\d]{2})', fun, url)
    # rule 5
    while re.search('(/\./)', url):
        url = re.sub('(/\./)', '/', url)
    while re.search('(/[\w\d]+/\.\./)', url):
        url = re.sub('(/[\w\d]+/\.\./)', '/', url)
    while re.search('(/\.$)', url):
        url = re.sub('(/\.$)', '', url)
    while re.search('(/[\w\d]+/\.\.$)', url):
        url = re.sub('(/[\w\d]+/\.\.$)', '', url)
    # rule 4
    url = re.sub(':80/', '/', url)
    url = re.sub(':80$', '', url)
    # rule 1
    url = url.lower()
    # rule 2
    while re.search('(%[a-z][a-z])', url):
        url = re.sub('(%[a-z][a-z])',
                     lambda x: x.groups()[0].upper(), url)
    while re.search('(%[a-z]\d)', url):
        url = re.sub('(%[a-z]\d)',
                     lambda x: x.groups()[0].upper(), url)
    while re.search('(%\d[a-z])', url):
        url = re.sub('(%\d[a-z])',
                     lambda x: x.groups()[0].upper(), url)
    return url

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") ==\
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio(u"http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
