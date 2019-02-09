import unittest

from pangram import check_pangram


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "The quick brown fox jumps over the lazy dog.", "answer": True},
            {"input": "ABCDEF", "answer": False},
            {"input": "abcdefghijklmnopqrstuvwxyz", "answer": True},
            {"input": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "answer": True},
            {"input": "abcdefghijklmnopqrstuvwxy", "answer": False},
            {
                "input": "Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!",
                "answer": True,
            },
            {
                "input": "As quirky joke, chefs won't pay devil magic zebra tax.",
                "answer": True,
            },
            {
                "input": "Six big devils from Japan quickly forgot how to walt.",
                "answer": False,
            },
        ],
        "Extra": [
            {
                "input": "!F]gatv]FZ;.MVl=wGC%nr*$np#'bn?}oIOa_YMf]MBQpB^Ndh_T/hw^D*hxcZVUp-ugO<nfC,N@:ag?TMby:A^*?qV_BK",
                "answer": False,
            },
            {
                "input": "bnC_XuknwTlVL..wvNU/*s%)*BjXi?<Q.swXDk,T(k>X<&ZieBhy&IRvxbHtr<%c%mUEcXD$WB$m<']Wfbzecee-!miZot"
                "A=&)#TPGfjDB$nw_LIZ!#JecokQ(LQK*JXKqyDSrHJSG?YTLOPfwW}Wiq=-mAi%%N]Tc(v^[TvN:XW&=@rK~CbC}|DySivVj",
                "answer": True,
            },
            {
                "input": "OGvkMBRgvDtaHBILRgTNuroYZcUkJqnAtstCXZytcQJzbpjhLoOKjQHrs"
                "ZKViqBAPrnqKWKNBtbCEmhSWJoCjqmachvVGEGlpAJh",
                "answer": False,
            },
            {"input": "a", "answer": False},
            {
                "input": "IlrCOiJHgmROZaMAXvvBRESnEkAgJKJPPXIUtjaVOxrnYJQQjjjQSiU"
                "eJNUXdHUqwvHRkzTjYhIhLkubPzMOPKYPIaRLCcSgFHga",
                "answer": True,
            },
            {
                "input": "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog."
                " Junk MTV quiz graced by fox whelps.",
                "answer": True,
            },
            {
                "input": "Brick quiz whangs jumpy veldt foks. Bright viksens jump; dozy fowl quack."
                " Quick wafting zephyrs veks bold Jim. Quick zephyrs blow, veksing daft Jim."
                " Seks-charged fop blew my junk TV quiz. How quickly daft jumping zebras veks."
                " Two driven jocks help faks my big quiz. Quick, Baz, get my woven flaks jodhpurs!"
                " Now faks quiz Jack! my brave ghost pled. Five quacking zephyrs jolt my waks bed. "
                "Flummoksed by job, kvetching W.",
                "answer": False,
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert check_pangram(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert check_pangram(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
