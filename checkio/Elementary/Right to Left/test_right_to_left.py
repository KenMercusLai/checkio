import unittest

from right_to_left import left_join


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ("left", "right", "left", "stop"),
                "answer": "left,left,left,stop",
            },
            {"input": ("bright aright", "ok"), "answer": "bleft aleft,ok"},
            {"input": ("brightness wright",), "answer": "bleftness wleft"},
            {"input": ("enough", "jokes"), "answer": "enough,jokes"},
        ],
        "Extra": [
            {"input": ("r", "i", "g", "h", "t"), "answer": "r,i,g,h,t"},
            {
                "input": (
                    'lorem',
                    'ipsum',
                    'dolor',
                    'sit',
                    'amet',
                    'consectetuer',
                    'adipiscing',
                    'elit',
                    'aenean',
                    'commodo',
                    'ligula',
                    'eget',
                    'dolor',
                    'aenean',
                    'massa',
                    'cum',
                    'sociis',
                    'natoque',
                    'penatibus',
                    'et',
                    'magnis',
                    'dis',
                    'parturient',
                    'montes',
                    'nascetur',
                    'ridiculus',
                    'mus',
                    'donec',
                    'quam',
                    'felis',
                    'ultricies',
                    'nec',
                    'pellentesque',
                    'eu',
                    'pretium',
                    'quis',
                    'sem',
                    'nulla',
                    'consequat',
                    'massa',
                    'quis',
                ),
                "answer": 'lorem,ipsum,dolor,sit,amet,consectetuer,adipiscing,'
                'elit,aenean,commodo,ligula,eget,dolor,aenean,massa,'
                'cum,sociis,natoque,penatibus,et,magnis,dis,'
                'parturient,montes,nascetur,ridiculus,mus,donec,quam'
                ',felis,ultricies,nec,pellentesque,eu,pretium,quis,'
                'sem,nulla,consequat,massa,quis',
            },
            {"input": ("right",) * 20, "answer": ",".join(("left",) * 20)},
            {"input": ("right", "left") * 10, "answer": ",".join(("left",) * 20)},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert left_join(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert left_join(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
