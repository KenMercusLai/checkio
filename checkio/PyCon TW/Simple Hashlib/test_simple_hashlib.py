import hashlib
import random
import unittest

from simple_hashlib import checkio


hashfunc_dic = {"md5": hashlib.md5,
                "sha224": hashlib.sha224,
                "sha256": hashlib.sha256,
                "sha256": hashlib.sha256,
                "sha384": hashlib.sha384,
                "sha512": hashlib.sha512,
                "sha1": hashlib.sha1}


def hash_text(t, func):
    return hashfunc_dic[func](bytes(t, "utf-8")).hexdigest()


result_list = []
for hash_f in hashfunc_dic:
    for i in range(40):
        t = ""
        for j in range(1, random.randint(1, 100)):
            t += chr(random.randint(32, 126))
        result_list.append({"input": (t, hash_f),
                            "answer": hash_text(t, hash_f)})


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ('welcome to pycon', 'md5'),
                "answer": hash_text('welcome to pycon', 'md5')
            },
            {
                "input": ('welcome to pycon', 'sha224'),
                "answer": hash_text('welcome to pycon', 'sha224')
            },
            {
                "input": ('welcome to pycon', 'sha256'),
                "answer": hash_text('welcome to pycon', 'sha256')
            },
            {
                "input": ('welcome to pycon', 'sha384'),
                "answer": hash_text('welcome to pycon', 'sha384')
            },
            {
                "input": ('welcome to pycon', 'sha512'),
                "answer": hash_text('welcome to pycon', 'sha512')
            },
            {
                "input": ('welcome to pycon', 'sha1'),
                "answer": hash_text('welcome to pycon', 'sha1')
            }

        ],
        "Extra": result_list
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
