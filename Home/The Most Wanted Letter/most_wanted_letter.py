from collections import defaultdict

def checkio(text):
    result = defaultdict(int)
    for i in text.lower():
        if 'a' <= i <= 'z':
            result[i] += 1

    # after having count numbers for all letter, sort them for the counter number the letter
    # bigger number first, if the number is the same, 'smaller' letter comes first
    return max(result, key=lambda x: '{0:0100000d}'.format(result[x])+chr(ord('z')-ord(x)+ord('a')))

if __name__ == '__main__': # pragma: no cover
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

