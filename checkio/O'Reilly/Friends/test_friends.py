import unittest

from friends import Friends


class Tests(unittest.TestCase):
    def test_Init(self):
        Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
        Friends([{"1", "2"}, {"3", "1"}])

    def test_Add(self):
        f = Friends([{"1", "2"}, {"3", "1"}])
        assert f.add({"2", "4"}) is True

        f = Friends([{"And", "Or"}, {"For", "And"}])
        assert f.add({"It", "Am"}) is True

        f = Friends([{"And", "Or"}, {"For", "And"}])
        assert f.add({"Or", "And"}) is False

    def test_Remove(self):
        f = Friends([{"1", "2"}, {"3", "1"}])
        assert f.remove({"2", "4"}) is False

        f = Friends([{"1", "2"}, {"3", "1"}])
        assert f.remove({"11", "12"}) is False

        f = Friends([{"And", "Or"}, {"For", "And"}])
        assert f.remove({"And", "Or"}) is True

    def test_Names(self):
        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        n = f.names()
        assert n == {"nikola", "sophia", "robot", "pilot", "stephen"}

        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        f.remove({"stephen", "robot"})
        n = f.names()
        assert n == {"nikola", "sophia", "pilot"}

    def test_Connected(self):
        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        n = f.connected("nikola")
        assert n == {"sophia"}

        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        n = f.connected("sophia")
        assert n == {"nikola", "pilot"}

        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        n = f.connected("DDD")
        assert n == set()

        f = Friends(({"nikola", "sophia"},
                     {"stephen", "robot"},
                     {"sophia", "pilot"}))
        f.add({"sophia", "stephen"})
        f.remove({"sophia", "nikola"})
        n = f.connected("sophia")
        assert n == {"stephen", "pilot"}
