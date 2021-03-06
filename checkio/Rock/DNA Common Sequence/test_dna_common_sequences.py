import unittest

from dna_common_sequences import common


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": ['ACGTC', 'TTACTC'], "answer": "ACTC"},
            {"input": ['TTACTC', 'ACGTC'], "answer": "ACTC"},
            {"input": ['CGCTA', 'TACCG'], "answer": "CC,CG,TA"},
            {"input": ['GCTT', 'AAAAA'], "answer": ""},
            {"input": ['CGTCGTCGT', 'CGTACGT'], "answer": "CGTCGT"},
            {
                "input": ['TGCAAAACGT', 'ACGTAAAATGCA'],
                "answer": "CAAAAC,CAAAAG,CAAAAT,GAAAAC,GAAAAG,GAAAAT,TAAAAC,TAAAAG,TAAAAT",
            },
            {"input": ['GGGCCCAAA', 'AAACCCGGGG'], "answer": "AAA,CCC,GGG"},
        ],
        "Extra": [
            {"input": ('TTGGTGTCGCTAGACC', 'CGCTAGTGGGGAAT'), "answer": "TTGGGGAA"},
            {
                "input": (
                    'GTCGCTGTGCAGGTCCGGGTTCA',
                    'GCGACCCGAATCCAGCTATAGGTATATGTCAGTCGGCCGTTAGGT',
                ),
                "answer": "GCGCGTGCAGGTCCGGGTTA,GTCGCTGTGCAGTCGGGTTA",
            },
            {
                "input": ('CCCATTCACGT', 'TGGCGACCGGGATCGTACTT'),
                "answer": "CCCATCACT,CCCATTACT",
            },
            {
                "input": ('CATATGTGTACTGC', 'GCCGACCGCTGTCATTAATATACAGTTCGAA'),
                "answer": "CATATTTACGC,CATATTTACTC,CATATTTACTG,CATATTTATGC",
            },
            {
                "input": (
                    'GGAGTACCATGGGCGGGACGTCACAGCCCCCAACTCA',
                    'AAGGTGACGCAAATGGTATATTCGCTAAGGATT',
                ),
                "answer": "AGTACCATGGACGCAAGAT,AGTACCATGGACGTAAGAT,AGTACCATGGATACGCAAA,AGTACCATGGATACGCAAT,AGTACCATGGCGCTAAGAT,GGGACCATGGACGCAAGAT,GGGACCATGGACGTAAGAT,GGGACCATGGATACGCAAA,GGGACCATGGATACGCAAT,GGGACCATGGCGCTAAGAT,GGTACCATGGACGCAAGAT,GGTACCATGGACGTAAGAT,GGTACCATGGATACGCAAA,GGTACCATGGATACGCAAT,GGTACCATGGCGCTAAGAT",
            },
            {
                "input": (
                    'TAGTCTTCTGGTCTAAATCCCTGCAGGAATATGCAAACTGG',
                    'TCCTGATCTCATGGT',
                ),
                "answer": "TCCTGATCTCAGGT,TCCTGATCTCATGG,TCCTGATCTCATGT",
            },
            {
                "input": ('AGTAATAATATGCTTCGGCTTTA', 'CGCGGGCAGTATC'),
                "answer": "CCGGCTA,CCGGCTT,GCGGCTA,GCGGCTT,GGGGCTA,GGGGCTT",
            },
            {
                "input": (
                    'AACGTTTTGGGTTTAGAGAAAGTGCTCACAGTAGGTACGTCCCCCAGACCCCACGCCAATGTAT',
                    'TTTGGGAATGCAATTTAGCTCACAGAGCATACAATGAGAACCACCGAGATCATATTAAGTCTCC',
                ),
                "answer": "TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATTAT",
            },
            {
                "input": (
                    'CATTCATTTACAACACTAGGGTAACACCAGCGCGATAGGCTGAGAAAACAC',
                    'CTCACCATTGAAGACAACCCGCTTGCGAACCGAAATGGTGACGGAACAACCCTCCCAGTT',
                ),
                "answer": "CACATTAAACAACCCGCGCGAAGGTGAGAAAACA,CACATTAAACAACCCGCGCGAAGGTGAGAAAACC,CACATTAAACAACCCGCGCGATGGTGAGAAAACA,CACATTAAACAACCCGCGCGATGGTGAGAAAACC,CACATTAAACAAGGCAACCGAAGGTGAGAAAACA,CACATTAAACAAGGCAACCGAAGGTGAGAAAACC,CACATTAAACAAGGCAACCGATGGTGAGAAAACA,CACATTAAACAAGGCAACCGATGGTGAGAAAACC,CACATTAAACAAGGGAACAAATGGTGAGAAAACA,CACATTAAACAAGGGAACAAATGGTGAGAAAACC,CACATTAAACAAGGGAACCAAAGGTGAGAAAACA,CACATTAAACAAGGGAACCAAAGGTGAGAAAACC,CACATTAAACAAGGGAACCAATGGTGAGAAAACA,CACATTAAACAAGGGAACCAATGGTGAGAAAACC,CACATTAAACAAGGGAACCGAAGGTGAGAAAACA,CACATTAAACAAGGGAACCGAAGGTGAGAAAACC,CACATTAAACAAGGGAACCGATGGTGAGAAAACA,CACATTAAACAAGGGAACCGATGGTGAGAAAACC,CACATTAAACAAGTCAACCGAAGGTGAGAAAACA,CACATTAAACAAGTCAACCGAAGGTGAGAAAACC,CACATTAAACAAGTCAACCGATGGTGAGAAAACA,CACATTAAACAAGTCAACCGATGGTGAGAAAACC,CACATTAAACACCCCGCGCGAAGGTGAGAAAACA,CACATTAAACACCCCGCGCGAAGGTGAGAAAACC,CACATTAAACACCCCGCGCGATGGTGAGAAAACA,CACATTAAACACCCCGCGCGATGGTGAGAAAACC,CACATTAAACACGGCAACCGAAGGTGAGAAAACA,CACATTAAACACGGCAACCGAAGGTGAGAAAACC,CACATTAAACACGGCAACCGATGGTGAGAAAACA,CACATTAAACACGGCAACCGATGGTGAGAAAACC,CACATTAAACACGGGAACAAATGGTGAGAAAACA,CACATTAAACACGGGAACAAATGGTGAGAAAACC,CACATTAAACACGGGAACCAAAGGTGAGAAAACA,CACATTAAACACGGGAACCAAAGGTGAGAAAACC,CACATTAAACACGGGAACCAATGGTGAGAAAACA,CACATTAAACACGGGAACCAATGGTGAGAAAACC,CACATTAAACACGGGAACCGAAGGTGAGAAAACA,CACATTAAACACGGGAACCGAAGGTGAGAAAACC,CACATTAAACACGGGAACCGATGGTGAGAAAACA,CACATTAAACACGGGAACCGATGGTGAGAAAACC,CACATTAAACACGTCAACCGAAGGTGAGAAAACA,CACATTAAACACGTCAACCGAAGGTGAGAAAACC,CACATTAAACACGTCAACCGATGGTGAGAAAACA,CACATTAAACACGTCAACCGATGGTGAGAAAACC,CACATTAAACACTGCAACCGAAGGTGAGAAAACA,CACATTAAACACTGCAACCGAAGGTGAGAAAACC,CACATTAAACACTGCAACCGATGGTGAGAAAACA,CACATTAAACACTGCAACCGATGGTGAGAAAACC,CACATTAAACACTGGAACAAATGGTGAGAAAACA,CACATTAAACACTGGAACAAATGGTGAGAAAACC,CACATTAAACACTGGAACCAAAGGTGAGAAAACA,CACATTAAACACTGGAACCAAAGGTGAGAAAACC,CACATTAAACACTGGAACCAATGGTGAGAAAACA,CACATTAAACACTGGAACCAATGGTGAGAAAACC,CACATTAAACACTGGAACCGAAGGTGAGAAAACA,CACATTAAACACTGGAACCGAAGGTGAGAAAACC,CACATTAAACACTGGAACCGATGGTGAGAAAACA,CACATTAAACACTGGAACCGATGGTGAGAAAACC,CACATTAAACACTTCAACCGAAGGTGAGAAAACA,CACATTAAACACTTCAACCGAAGGTGAGAAAACC,CACATTAAACACTTCAACCGATGGTGAGAAAACA,CACATTAAACACTTCAACCGATGGTGAGAAAACC,CACATTACAACCGGCAACCGAAGGTGAGAAAACA,CACATTACAACCGGCAACCGAAGGTGAGAAAACC,CACATTACAACCGGCAACCGATGGTGAGAAAACA,CACATTACAACCGGCAACCGATGGTGAGAAAACC,CACATTACAACCGGGAACAAATGGTGAGAAAACA,CACATTACAACCGGGAACAAATGGTGAGAAAACC,CACATTACAACCGGGAACCAAAGGTGAGAAAACA,CACATTACAACCGGGAACCAAAGGTGAGAAAACC,CACATTACAACCGGGAACCAATGGTGAGAAAACA,CACATTACAACCGGGAACCAATGGTGAGAAAACC,CACATTACAACCGGGAACCGAAGGTGAGAAAACA,CACATTACAACCGGGAACCGAAGGTGAGAAAACC,CACATTACAACCGGGAACCGATGGTGAGAAAACA,CACATTACAACCGGGAACCGATGGTGAGAAAACC,CACATTACAACCGTCAACCGAAGGTGAGAAAACA,CACATTACAACCGTCAACCGAAGGTGAGAAAACC,CACATTACAACCGTCAACCGATGGTGAGAAAACA,CACATTACAACCGTCAACCGATGGTGAGAAAACC,CACATTACAACCTGCAACCGAAGGTGAGAAAACA,CACATTACAACCTGCAACCGAAGGTGAGAAAACC,CACATTACAACCTGCAACCGATGGTGAGAAAACA,CACATTACAACCTGCAACCGATGGTGAGAAAACC,CACATTACAACCTGGAACAAATGGTGAGAAAACA,CACATTACAACCTGGAACAAATGGTGAGAAAACC,CACATTACAACCTGGAACCAAAGGTGAGAAAACA,CACATTACAACCTGGAACCAAAGGTGAGAAAACC,CACATTACAACCTGGAACCAATGGTGAGAAAACA,CACATTACAACCTGGAACCAATGGTGAGAAAACC,CACATTACAACCTGGAACCGAAGGTGAGAAAACA,CACATTACAACCTGGAACCGAAGGTGAGAAAACC,CACATTACAACCTGGAACCGATGGTGAGAAAACA,CACATTACAACCTGGAACCGATGGTGAGAAAACC,CACATTACAACCTTCAACCGAAGGTGAGAAAACA,CACATTACAACCTTCAACCGAAGGTGAGAAAACC,CACATTACAACCTTCAACCGATGGTGAGAAAACA,CACATTACAACCTTCAACCGATGGTGAGAAAACC,CTCACCATAAACACCGCGCGAAGGTGAGAAAACA,CTCACCATAAACACCGCGCGAAGGTGAGAAAACC,CTCACCATAAACACCGCGCGATGGTGAGAAAACA,CTCACCATAAACACCGCGCGATGGTGAGAAAACC,CTCACCATAGAAACCGCGCGAAGGTGAGAAAACA,CTCACCATAGAAACCGCGCGAAGGTGAGAAAACC,CTCACCATAGAAACCGCGCGATGGTGAGAAAACA,CTCACCATAGAAACCGCGCGATGGTGAGAAAACC,CTCACCATAGAACCCGCGCGAAGGTGAGAAAACA,CTCACCATAGAACCCGCGCGAAGGTGAGAAAACC,CTCACCATAGAACCCGCGCGATGGTGAGAAAACA,CTCACCATAGAACCCGCGCGATGGTGAGAAAACC,CTCACCATAGACACCGCGCGAAGGTGAGAAAACA,CTCACCATAGACACCGCGCGAAGGTGAGAAAACC,CTCACCATAGACACCGCGCGATGGTGAGAAAACA,CTCACCATAGACACCGCGCGATGGTGAGAAAACC,CTCACCATGAACACCGCGCGAAGGTGAGAAAACA,CTCACCATGAACACCGCGCGAAGGTGAGAAAACC,CTCACCATGAACACCGCGCGATGGTGAGAAAACA,CTCACCATGAACACCGCGCGATGGTGAGAAAACC,CTCACCATGGAAACCGCGCGAAGGTGAGAAAACA,CTCACCATGGAAACCGCGCGAAGGTGAGAAAACC,CTCACCATGGAAACCGCGCGATGGTGAGAAAACA,CTCACCATGGAAACCGCGCGATGGTGAGAAAACC,CTCACCATGGAACCCGCGCGAAGGTGAGAAAACA,CTCACCATGGAACCCGCGCGAAGGTGAGAAAACC,CTCACCATGGAACCCGCGCGATGGTGAGAAAACA,CTCACCATGGAACCCGCGCGATGGTGAGAAAACC,CTCACCATGGACACCGCGCGAAGGTGAGAAAACA,CTCACCATGGACACCGCGCGAAGGTGAGAAAACC,CTCACCATGGACACCGCGCGATGGTGAGAAAACA,CTCACCATGGACACCGCGCGATGGTGAGAAAACC,CTCACCATTAACACCGCGCGAAGGTGAGAAAACA,CTCACCATTAACACCGCGCGAAGGTGAGAAAACC,CTCACCATTAACACCGCGCGATGGTGAGAAAACA,CTCACCATTAACACCGCGCGATGGTGAGAAAACC,CTCATTAAACAACCCGCGCGAAGGTGAGAAAACA,CTCATTAAACAACCCGCGCGAAGGTGAGAAAACC,CTCATTAAACAACCCGCGCGATGGTGAGAAAACA,CTCATTAAACAACCCGCGCGATGGTGAGAAAACC,CTCATTAAACAAGGCAACCGAAGGTGAGAAAACA,CTCATTAAACAAGGCAACCGAAGGTGAGAAAACC,CTCATTAAACAAGGCAACCGATGGTGAGAAAACA,CTCATTAAACAAGGCAACCGATGGTGAGAAAACC,CTCATTAAACAAGGGAACAAATGGTGAGAAAACA,CTCATTAAACAAGGGAACAAATGGTGAGAAAACC,CTCATTAAACAAGGGAACCAAAGGTGAGAAAACA,CTCATTAAACAAGGGAACCAAAGGTGAGAAAACC,CTCATTAAACAAGGGAACCAATGGTGAGAAAACA,CTCATTAAACAAGGGAACCAATGGTGAGAAAACC,CTCATTAAACAAGGGAACCGAAGGTGAGAAAACA,CTCATTAAACAAGGGAACCGAAGGTGAGAAAACC,CTCATTAAACAAGGGAACCGATGGTGAGAAAACA,CTCATTAAACAAGGGAACCGATGGTGAGAAAACC,CTCATTAAACAAGTCAACCGAAGGTGAGAAAACA,CTCATTAAACAAGTCAACCGAAGGTGAGAAAACC,CTCATTAAACAAGTCAACCGATGGTGAGAAAACA,CTCATTAAACAAGTCAACCGATGGTGAGAAAACC,CTCATTAAACACCCCGCGCGAAGGTGAGAAAACA,CTCATTAAACACCCCGCGCGAAGGTGAGAAAACC,CTCATTAAACACCCCGCGCGATGGTGAGAAAACA,CTCATTAAACACCCCGCGCGATGGTGAGAAAACC,CTCATTAAACACGGCAACCGAAGGTGAGAAAACA,CTCATTAAACACGGCAACCGAAGGTGAGAAAACC,CTCATTAAACACGGCAACCGATGGTGAGAAAACA,CTCATTAAACACGGCAACCGATGGTGAGAAAACC,CTCATTAAACACGGGAACAAATGGTGAGAAAACA,CTCATTAAACACGGGAACAAATGGTGAGAAAACC,CTCATTAAACACGGGAACCAAAGGTGAGAAAACA,CTCATTAAACACGGGAACCAAAGGTGAGAAAACC,CTCATTAAACACGGGAACCAATGGTGAGAAAACA,CTCATTAAACACGGGAACCAATGGTGAGAAAACC,CTCATTAAACACGGGAACCGAAGGTGAGAAAACA,CTCATTAAACACGGGAACCGAAGGTGAGAAAACC,CTCATTAAACACGGGAACCGATGGTGAGAAAACA,CTCATTAAACACGGGAACCGATGGTGAGAAAACC,CTCATTAAACACGTCAACCGAAGGTGAGAAAACA,CTCATTAAACACGTCAACCGAAGGTGAGAAAACC,CTCATTAAACACGTCAACCGATGGTGAGAAAACA,CTCATTAAACACGTCAACCGATGGTGAGAAAACC,CTCATTAAACACTGCAACCGAAGGTGAGAAAACA,CTCATTAAACACTGCAACCGAAGGTGAGAAAACC,CTCATTAAACACTGCAACCGATGGTGAGAAAACA,CTCATTAAACACTGCAACCGATGGTGAGAAAACC,CTCATTAAACACTGGAACAAATGGTGAGAAAACA,CTCATTAAACACTGGAACAAATGGTGAGAAAACC,CTCATTAAACACTGGAACCAAAGGTGAGAAAACA,CTCATTAAACACTGGAACCAAAGGTGAGAAAACC,CTCATTAAACACTGGAACCAATGGTGAGAAAACA,CTCATTAAACACTGGAACCAATGGTGAGAAAACC,CTCATTAAACACTGGAACCGAAGGTGAGAAAACA,CTCATTAAACACTGGAACCGAAGGTGAGAAAACC,CTCATTAAACACTGGAACCGATGGTGAGAAAACA,CTCATTAAACACTGGAACCGATGGTGAGAAAACC,CTCATTAAACACTTCAACCGAAGGTGAGAAAACA,CTCATTAAACACTTCAACCGAAGGTGAGAAAACC,CTCATTAAACACTTCAACCGATGGTGAGAAAACA,CTCATTAAACACTTCAACCGATGGTGAGAAAACC,CTCATTACAACCGGCAACCGAAGGTGAGAAAACA,CTCATTACAACCGGCAACCGAAGGTGAGAAAACC,CTCATTACAACCGGCAACCGATGGTGAGAAAACA,CTCATTACAACCGGCAACCGATGGTGAGAAAACC,CTCATTACAACCGGGAACAAATGGTGAGAAAACA,CTCATTACAACCGGGAACAAATGGTGAGAAAACC,CTCATTACAACCGGGAACCAAAGGTGAGAAAACA,CTCATTACAACCGGGAACCAAAGGTGAGAAAACC,CTCATTACAACCGGGAACCAATGGTGAGAAAACA,CTCATTACAACCGGGAACCAATGGTGAGAAAACC,CTCATTACAACCGGGAACCGAAGGTGAGAAAACA,CTCATTACAACCGGGAACCGAAGGTGAGAAAACC,CTCATTACAACCGGGAACCGATGGTGAGAAAACA,CTCATTACAACCGGGAACCGATGGTGAGAAAACC,CTCATTACAACCGTCAACCGAAGGTGAGAAAACA,CTCATTACAACCGTCAACCGAAGGTGAGAAAACC,CTCATTACAACCGTCAACCGATGGTGAGAAAACA,CTCATTACAACCGTCAACCGATGGTGAGAAAACC,CTCATTACAACCTGCAACCGAAGGTGAGAAAACA,CTCATTACAACCTGCAACCGAAGGTGAGAAAACC,CTCATTACAACCTGCAACCGATGGTGAGAAAACA,CTCATTACAACCTGCAACCGATGGTGAGAAAACC,CTCATTACAACCTGGAACAAATGGTGAGAAAACA,CTCATTACAACCTGGAACAAATGGTGAGAAAACC,CTCATTACAACCTGGAACCAAAGGTGAGAAAACA,CTCATTACAACCTGGAACCAAAGGTGAGAAAACC,CTCATTACAACCTGGAACCAATGGTGAGAAAACA,CTCATTACAACCTGGAACCAATGGTGAGAAAACC,CTCATTACAACCTGGAACCGAAGGTGAGAAAACA,CTCATTACAACCTGGAACCGAAGGTGAGAAAACC,CTCATTACAACCTGGAACCGATGGTGAGAAAACA,CTCATTACAACCTGGAACCGATGGTGAGAAAACC,CTCATTACAACCTTCAACCGAAGGTGAGAAAACA,CTCATTACAACCTTCAACCGAAGGTGAGAAAACC,CTCATTACAACCTTCAACCGATGGTGAGAAAACA,CTCATTACAACCTTCAACCGATGGTGAGAAAACC",
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert common(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert common(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
