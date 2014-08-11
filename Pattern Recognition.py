def checkio(pattern, image):
    patternWidth = len(pattern[0])
    patternHeight = len(pattern)
    for y in range(len(image) - patternHeight + 1):
        for x in range(len(image[0]) - patternWidth + 1):
            tempMatrix = []
            # take sub matrix
            for i in range(patternHeight):
                tempMatrix.append(image[y + i][x:x + patternWidth])
            if tempMatrix == pattern:
                for i in range(patternHeight):
                    image[y + i][x:x + patternWidth] = map(lambda x: x + 2,
                                                           image[y + i][x:x + patternWidth])
    return image

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == \
        [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
