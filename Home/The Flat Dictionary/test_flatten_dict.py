import unittest
from flatten_dict import flatten


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": {"key": "value"},
                "answer": {"key": "value"},
            },
            {
                "input": {"key": {"deeper": {"more": {"enough": "value"}}}},
                "answer": {"key/deeper/more/enough": "value"},
            },
            {
                "input": {"empty": {}},
                "answer": {"empty": ""},
            },
            {
                "input": {"name": {
                    "first": "One",
                    "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                    "place": {
                        "zone": "1",
                        "cell": "2"}}},
                "answer": {"name/first": "One",
                           "name/last": "Drone",
                           "job": "scout",
                           "recent": "",
                           "additional/place/zone": "1",
                           "additional/place/cell": "2"},
            },
        ],
        "Extra": [
            {
                "input": {"name": {
                    "first": "Second",
                    "last": "Drone",
                    "nick": {}
                },
                    "job": {
                    "1": "scout",
                    "2": "worker",
                    "3": "writer",
                    "4": "reader",
                    "5": "learner",

                },
                    "recent": {
                    "places": {
                        "earth": {
                            "Louvre": "2015",
                            "NY": "2017",
                                  "NP": "",
                        }
                    },
                    "times": {
                        "XX": {
                            "1964": "Yes"
                        },
                        "XXI": {
                            "2064": "Nope",
                        }
                    }
                }},
                "answer": {"job/1": "scout", "recent/places/earth/NY": "2017", "job/3": "writer", "job/2": "worker",
                           "job/5": "learner", "job/4": "reader", "recent/places/earth/NP": "",
                           "recent/places/earth/Louvre": "2015", "recent/times/XX/1964": "Yes",
                           "recent/times/XXI/2064": "Nope", "name/first": "Second", "name/last": "Drone", "name/nick": ""},
            },
            {
                "input": {"Hm": {"What": {"is": {"here": {"?": {}}}}}},
                "answer": {"Hm/What/is/here/?": ""},
            },
            {
                "input": {"flat": "yep",
                          "root": "yep",
                          "who": "iam"},
                "answer": {"flat": "yep",
                           "root": "yep",
                           "who": "iam"},
            },
            {
                "input": {"1": "X",
                          "3": {"31": {
                              "312": "V"
                          },
                              "34": {
                              "345": {
                                  "3458": {
                                      "34580": "X"
                                  }
                              }
                          }}},
                "answer": {"1": "X", "3/31/312": "V", "3/34/345/3458/34580": "X"},
            },
            {
                "input": {
                    "glossary": {
                        "title": "example glossary",
                        "GlossDiv": {
                            "title": "S",
                            "GlossList": {
                                "GlossEntry": {
                                    "ID": "SGML",
                                    "SortAs": "SGML",
                                    "GlossTerm": "Standard Generalized Markup Language",
                                    "Acronym": "SGML",
                                    "Abbrev": "ISO 8879:1986",
                                    "GlossDef": {
                                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                        "GlossSeeAlso": {"1": "GML", "2": "XML"}
                                    },
                                    "GlossSee": "markup"
                                }
                            }
                        }
                    },
                    "source": "http://json.org/example"
                },
                "answer": {
                    "glossary/GlossDiv/GlossList/GlossEntry/GlossDef/para": "A meta-markup language, used to create markup languages such as DocBook.",
                    "glossary/title": "example glossary", "glossary/GlossDiv/GlossList/GlossEntry/Abbrev": "ISO 8879:1986",
                    "glossary/GlossDiv/GlossList/GlossEntry/SortAs": "SGML",
                    "glossary/GlossDiv/GlossList/GlossEntry/Acronym": "SGML",
                    "glossary/GlossDiv/GlossList/GlossEntry/GlossTerm": "Standard Generalized Markup Language",
                    "glossary/GlossDiv/title": "S", "source": "http://json.org/example",
                    "glossary/GlossDiv/GlossList/GlossEntry/GlossDef/GlossSeeAlso/2": "XML",
                    "glossary/GlossDiv/GlossList/GlossEntry/ID": "SGML",
                    "glossary/GlossDiv/GlossList/GlossEntry/GlossDef/GlossSeeAlso/1": "GML",
                    "glossary/GlossDiv/GlossList/GlossEntry/GlossSee": "markup"},
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert flatten(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert flatten(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
