from itertools import product


def get_matched_positions(text, keywords):
    results = []
    for i in keywords:
        if i:
            index = 0
            while index < len(text):
                index = text.find(i, index)
                if index == -1:
                    break
                results.append((index, index + len(i)))
                index += len(i)
    return results


def positions_overlapped(position1, position2, text):
    return any(
        [
            position1[1] > position2[0],
            position1[1] == position2[0]
            and text[position1[0] : position1[1]] == text[position2[0] : position2[1]],
        ]
    )


def merge_positions(position1, position2):
    return (min(position1[0], position2[0]), max(position1[1], position2[1]))


def checkio(text, words):
    matched_positions = get_matched_positions(
        text.lower(), [i.lower() for i in words.split(' ')]
    )
    positions_updated = True
    sorted_positions = sorted(matched_positions)
    while positions_updated:
        positions_updated = False
        for index, value in enumerate(sorted_positions[:-1]):
            for i in product([value], sorted_positions[index + 1 :]):
                if positions_overlapped(i[0], i[1], text):
                    sorted_positions.remove(i[0])
                    sorted_positions.remove(i[1])
                    sorted_positions.append(merge_positions(*i))
                    sorted_positions = sorted(sorted_positions)
                    positions_updated = True
                    break
            if positions_updated:
                break
    reversed_positions = sorted(sorted_positions, reverse=True)
    for i in reversed_positions:
        text = text[: i[0]] + '<span>' + text[i[0] : i[1]] + '</span>' + text[i[1] :]
    return text


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':  # pragma: no cover
    assert (
        checkio("This is only a text example for task example.", "example")
        == "This is only a text <span>example</span> for task <span>example</span>."
    ), "Simple test"

    assert (
        checkio("Python is a widely used high-level programming language.", "pyThoN")
        == "<span>Python</span> is a widely used high-level programming language."
    ), "Ignore letters cases, but keep original"

    assert (
        checkio(
            "It is experiment for control groups with similar distributions.", "is im"
        )
        == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."
    ), "Several subwords"

    assert (
        checkio(
            "The National Aeronautics and Space Administration (NASA).", "nasa  THE"
        )
        == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."
    ), "two spaces"

    assert (
        checkio("Did you find anything?", "word space tree") == "Did you find anything?"
    ), "No comments"

    assert (
        checkio("Hello World! Or LOL", "hell world or lo")
        == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
    ), "Contain or intersect"
