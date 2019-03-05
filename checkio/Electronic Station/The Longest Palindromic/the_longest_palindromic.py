def is_palindromic(text):
    index = 0
    while index < len(text) / 2:
        if text[index] != text[len(text) - index - 1]:
            return False
        index += 1
    return True


def yield_substring(text, ele):
    # return substring of given text with ele as the first & last char
    indexes = [i for i in range(len(text)) if text[i] == ele]
    for i in range(len(indexes) - 1):
        for j in range(i + 1, len(indexes)):
            yield text[indexes[i] : indexes[j] + 1]


def longest_palindromic(text):
    text_elements = set(text)
    palindromic = text[0]
    for i in text_elements:
        for j in yield_substring(text, i):
            if is_palindromic(j):
                if len(j) == len(palindromic) and text.find(j) < text.find(palindromic):
                    palindromic = j
                elif len(j) > len(palindromic):
                    palindromic = j
    return palindromic


if __name__ == '__main__':  # pragma: no cover
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
