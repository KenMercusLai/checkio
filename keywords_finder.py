def get_matched_positions(text, word_list):
    """get all matched positions

    Args:
        text (str): Description
        word_list (list): a list of keywords in lowercase

    Returns:
        list: list of tuples for start and end position contain matched words
    """
    results = []
    for i in word_list:
        start_position = 0
        temp_results = []
        word_length = len(i)
        matched = text.find(i, 0)
        while matched != -1:
            temp_results.append((matched, matched + word_length - 1))
            start_position += matched + word_length
            matched = text.find(i, start_position)
        results += merge_contiguities(temp_results, False)
    return results


def is_contiguious(pair1, pair2):
    if pair1[0] > pair2[1] + 1 or pair2[0] > pair1[1] + 1:
        return False
    return True


def is_overlapped(pair1, pair2):
    if (pair1[0] <= pair2[0] <= pair1[1]
            or pair1[0] <= pair2[1] <= pair1[1]
            or pair2[0] <= pair1[0] <= pair2[1]
            or pair2[0] <= pair1[1] <= pair2[1]):
        return True
    return False


def merge_contiguities(matched_pairs, strict):
    changed = True
    while changed:
        changed = False
        for i in range(len(matched_pairs)):
            for j in range(i + 1, len(matched_pairs)):
                pair1, pair2 = matched_pairs[i], matched_pairs[j]
                if (not strict and is_contiguious(pair1, pair2)) or (strict and is_overlapped(pair1, pair2)):
                    new_pair = (
                        min(pair1[0], pair2[0]), max(pair1[1], pair2[1]))
                    matched_pairs.remove(pair1)
                    matched_pairs.remove(pair2)
                    matched_pairs.append(new_pair)
                    changed = True
                if changed:
                    break
            if changed:
                break
    return matched_pairs


def checkio(text, words):
    matched_pairs = get_matched_positions(
        text.lower(), [i.lower() for i in words.split()])
    for i in sorted(merge_contiguities(matched_pairs, True), reverse=True):
        temp_text = list(text)
        temp_text.insert(i[1] + 1, '</span>')
        temp_text.insert(i[0], '<span>')
        text = ''.join(temp_text)
    return text

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__': # pragma: no cover
    assert (checkio("This is only a text example for task example.", "example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"
