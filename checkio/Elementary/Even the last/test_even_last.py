import unittest

from even_last import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [0, 1, 2, 3, 4, 5],
                "answer": 30,
                "explanation": "5*(0+2+4)"
            },
            {
                "input": [1, 3, 5],
                "answer": 30,
                "explanation": "5*(1+5)"
            },
            {
                "input": [6],
                "answer": 36,
                "explanation": "6*(6)"
            },
            {
                "input": [],
                "answer": 0,
                "explanation": "The empty array"
            }
        ],
        "Extra": [
            {
                "input": [-45],
                "answer": 2025,
                "explanation": "-45*(-45)"
            },
            {
                "input": [-89, -86, 13, -69, 94, -75, 66, 97, -50],
                "answer": -1700,
                "explanation": "-50*(-89+13+94+66-50)"
            },
            {
                "input": [-78, -16, 84, 72, 33, -3, -9, -90, 13, -64,
                          10, -47, 99, -27, -87, -18, 76, -63],
                "answer": -8883,
                "explanation": "-63*(-78+84+33-9+13+10+99-87+76)"
            },
            {
                "input": [-40, 51, -71, -12, 24, -95, 20, 8, 68, -87, 28, 89,
                          -1, 61, 40, 56, 16, 0],
                "answer": 0,
                "explanation": "0*(-40-71+24+20+68+28-1+40+16)"
            },
            {
                "input": [60, -74, 18, -31, 90, 5, -86, -26],
                "answer": -2132,
                "explanation": "-26*(60+18+90-86)"
            },
            {
                "input": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 24],
                "answer": 0,
                "explanation": "24*(0+0+0+0+0+0+0+0+0+0)"
            },
            {
                "input": [-5, 94, 5, -28, 17, -72, 84, 85, -17, -96, -84, -76,
                          0, 75],
                "answer": 0,
                "explanation": "75*(-5+5+17+84-17-84+0)"
            },
            {
                "input": [-94, 21, -58, 38, 56, 6, -91, -69, 39],
                "answer": -5772,
                "explanation": "39*(-94-58+56-91+39)"
            },
            {
                "input": [28, 54, -7, 90, 64],
                "answer": 5440,
                "explanation": "64*(28-7+64)"
            },
            {
                "input": [39],
                "answer": 1521,
                "explanation": "39*(39)"
            },
            {
                "input": [-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62,
                          26, -76, 55, -24, 84, 49, -65, 41],
                "answer": 1968,
                "explanation": "41*(-37-19+29+3-64+36+26+55+84-65)"
            },
            {
                "input": [43, 91, -86, 64, 25, -85, -71, -73, 23, 89, 10, 21,
                          -78],
                "answer": 10452,
                "explanation": "-78*(43-86+25-71+23+10-78)"
            },
            {
                "input": [-36, 82, -14, 82, -59, -35, -39, 33, 28, 27, -24, 6,
                          83, 39, 85, 58, -44, -18, -90, -75],
                "answer": 8250,
                "explanation": "-75*(-36-14-59-39+28-24+83+85-44-90)"
            },
            {
                "input": [69, -91, -49, -29, 13, -42, 34, -99, -97, -80, 16,
                          -9],
                "answer": 126,
                "explanation": "-9*(69-49+13+34-97+16)"
            },
            {
                "input": [-43, -72, 3, -83, -82, 93, -59, -80, 6, -39, 16, 39,
                          1, 47, -19, 67, 51],
                "answer": -6426,
                "explanation": "51*(-43+3-82-59+6+16+1-19+51)"
            },
            {
                "input": [-80, -32, 52, -53, -21, -57, -58, -24, -15, -14, 97,
                          -79, -35, 69],
                "answer": -4140,
                "explanation": "69*(-80+52-21-58-15+97-35)"
            },
            {
                "input": [-77, -87, -10, 98, -65, -75, -26, -46, -54, 70, -52,
                          -81, -94, 46],
                "answer": -17388,
                "explanation": "46*(-77-10-65-26-54-52-94)"
            },
            {
                "input": [-88, 53, 55, -74, -36, 20, 95, -22, -63, -53, -68],
                "answer": 7140,
                "explanation": "-68*(-88+55-36+95-63-68)"
            },
            {
                "input": [45],
                "answer": 2025,
                "explanation": "45*(45)"
            },
            {
                "input": [72, -19, -73, -59, 83, -79, -90],
                "answer": 720,
                "explanation": "-90*(72-73+83-90)"
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
