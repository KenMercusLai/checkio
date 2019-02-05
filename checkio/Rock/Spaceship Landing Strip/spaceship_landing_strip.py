def checkio(landing_map):
    new_map = [(i.replace('G', '1').replace('S', '1').replace('R', '0')
                .replace('W', '0').replace('T', '0'))
               for i in landing_map]
    columns = len(new_map[0])
    rows = len(new_map)
    maxsize = 0
    for y in range(rows):
        for x in range(columns):
            for y2 in range(y, rows):
                for x2 in range(x, columns):
                    if (abs(y - y2) + 1) * (abs(x - x2) + 1) <= maxsize:
                        continue
                    else:
                        sub_map_string = ''.join([new_map[i][x:x2 + 1]
                                                  for i in range(y, y2 + 1)])
                        if '0' not in sub_map_string:
                            maxsize = sub_map_string.count('1')
    return maxsize


if __name__ == '__main__':
    assert checkio(['G']) == 1, 'First'
    assert checkio(['GS', 'GS']) == 4, 'Second'
    assert checkio(['GT', 'GG']) == 2, 'Third'
    assert checkio(['GGTGG', 'TGGGG', 'GSSGT', 'GGGGT',
                    'GWGGG', 'RGTRT', 'RTGWT', 'WTWGR']) == 9, 'Fourth'
    print('All is ok')
