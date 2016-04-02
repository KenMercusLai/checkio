import unittest

from monkey_typing import count_words


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ['How aresjfhdskfhskd you?',
                          ['how', 'are', 'you', 'hello']],
                "answer": 3,
                "show": "'How aresjfhdskfhskd you?', "
                        "{'you', 'how', 'hello', 'are'}",
                "explanation": '<strong>How</strong> <strong>are</strong>'
                               'sjfhdskfhskd <strong>you</strong>?'
            },
            {
                "input": ['Bananas, give me bananas!!!',
                          ['banana', 'bananas']],
                "answer": 2,
                "show": "'Bananas, give me bananas!!!', {'banana', 'bananas'}",
                "explanation": '<strong>Bananas</strong>, give me '
                               '<strong>bananas</strong>!!!'
            },
            {
                "input": ['Lorem ipsum dolor sit amet, consectetuer adipiscing'
                          ' elit.',
                          ['sum', 'hamlet', 'infinity', 'anything']],
                "answer": 1,
                "show": "'Lorem ipsum dolor sit amet, consectetuer adipiscing "
                        "elit.', {'hamlet', 'sum', 'infinity', 'anything'}",
                "explanation": 'Lorem ip<strong>sum</strong> dolor sit amet, '
                               'consectetuer adipiscing elit.'
            },
        ],
        "Edge": [
            {
                "input": ['A', ['the']],
                "answer": 0,
                "show": "A, {'the'}",
                "explanation": 'A'
            },
            {
                "input": ['PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatDz'
                          'edINMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdC'
                          'kFdjYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKppt'
                          'HbXuZwFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJj'
                          'deTSHuhJRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUh'
                          'm',
                          ['the', 'who', 'any', 'man', 'hey', 'box', 'zed']],
                "answer": 1,
                "show": "'PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXmgatDze"
                        "dINMmRVxWCIeUfXShDvlWCQtgGYXOxsFpdlNHhxUBRAwAZqXdCkFd"
                        "jYhBGwpVwJngGxgTDdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZ"
                        "wFKBAwCGiXNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuh"
                        "JRvUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm', {'man"
                        "', 'who', 'the', 'any', 'zed', 'hey', 'box'}",
                "explanation": 'PWEtRJYqAKYqMcnJxZSStUOyAJkvdtRgdBxnPpXZkBBZXm'
                               'gatD<strong>zed</strong>INMmRVxWCIeUfXShDvlWCQ'
                               'tgGYXOxsFpdlNHhxUBRAwAZqXdCkFdjYhBGwpVwJngGxgT'
                               'DdBHVDdufWGbdENvxbOMylqdPWBiKpptHbXuZwFKBAwCGi'
                               'XNkWxdHwadOqduygveRsmWfpjEWAztZyoLLJjdeTSHuhJR'
                               'vUjNDPZyJLseXUROuedMIiudevXESwFjuZACswxnUhm'
            },
        ],
        "Extra": [
            {
                "input": ['LOLOLOLOLOL', ['lol', 'olo']],
                "answer": 2,
                "show": "'LOLOLOLOLOL', {'lol', 'olo'}",
                "explanation": '<strong>LOLOLOLOLOL</strong>'
            },
            {
                "input": ['ab cd', ['abc']],
                "answer": 0,
                "show": "'ab cd', {'abc'}",
                "explanation": 'ab cd'
            },
            {
                "input": ['Oooooooooooo Thhhhe', ['the', 'hey']],
                "answer": 0,
                "show": "'Oooooooooooo Thhhhe', {'hey', 'the'}",
                "explanation": 'Oooooooooooo Thhhhe'
            },
            {
                "input": ['Far far away, behind the word mountains, far from '
                          'the countries Vokalia and Consonantia, there live '
                          'the blind texts.',
                          ['far', 'word', 'vokal', 'count', 'tries']],
                "answer": 5,
                "show": "'Far far away, behind the word mountains, far from "
                        "the countries Vokalia and Consonantia, there live the"
                        " blind texts.', {'far', 'word', 'count', 'vokal', "
                        "'tries'}",
                "explanation": '<strong>Far</strong> <strong>far</strong> '
                               'away, behind the <strong>word</strong> '
                               'mountains, <strong>far</strong> from the '
                               '<strong>countries</strong> <strong>Vokal'
                               '</strong>ia and Consonantia, there live the '
                               'blind texts.'
            },
            {
                "input": ['The quick, brown fox jumps over a lazy dog. DJs '
                          'flock by when MTV ax quiz prog. Junk MTV quiz '
                          'graced by fox whelps.',
                          ['nobody', 'hamlet', 'sophia', 'nikola', 'stephan']],
                "answer": 0,
                "show": "'The quick, brown fox jumps over a lazy dog. DJs "
                        "flock by when MTV ax quiz prog. Junk MTV quiz graced "
                        "by fox whelps.', {'nobody', 'sophia', 'nikola', "
                        "'hamlet', 'stephan'}",
                "explanation": 'The quick, brown fox jumps over a lazy dog. '
                               'DJs flock by when MTV ax quiz prog. Junk MTV '
                               'quiz graced by fox whelps.'
            },
            {
                "input": ['But I must explain to you how all this mistaken '
                          'idea of denouncing pleasure and praising pain was '
                          'born',
                          ['this', 'that', 'they', 'she', 'hello', 'world']],
                "answer": 1,
                "show": "'But I must explain to you how all this mistaken idea"
                        " of denouncing pleasure and praising pain was born', "
                        "{'this', 'world', 'she', 'hello', 'they', 'that'}",
                "explanation": 'But I must explain to you how all <strong>this'
                               '</strong> mistaken idea of denouncing pleasure'
                               ' and praising pain was born'
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert count_words(*i['input']) == i['answer'], i['input']

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert count_words(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert count_words(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
