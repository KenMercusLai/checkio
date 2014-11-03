def checkio(landing_map):
    NewMap = [(i.replace('G', '1').replace('S', '1').replace('R', '0').
               replace('W', '0').replace('T', '0'))
              for i in landing_map]
    Columns = len(NewMap[0])
    Rows = len(NewMap)
    MaxSize = 0
    for y in xrange(Rows):
        for x in xrange(Columns):
            for y2 in xrange(y, Rows):
                for x2 in xrange(x, Columns):
                    if (abs(y - y2) + 1) * (abs(x - x2) + 1) <= MaxSize:
                        continue
                    else:
                        SubMapString = ''.join([NewMap[i][x:x2 + 1]
                                                for i in xrange(y, y2 + 1)])
                        if '0' not in SubMapString:
                            MaxSize = SubMapString.count('1')
    return MaxSize

if __name__ == '__main__':
    assert checkio(['G']) == 1, 'First'
    assert checkio(['GS', 'GS']) == 4, 'Second'
    assert checkio(['GT', 'GG']) == 2, 'Third'
    assert checkio(['GGTGG', 'TGGGG', 'GSSGT', 'GGGGT',
                    'GWGGG', 'RGTRT', 'RTGWT', 'WTWGR']) == 9, 'Fourth'
    print 'All is ok'
