# def a_factaral(n):
#     if n == 0:
#         return 1
#     return n * a_factaral(n - 1)

a_factaral = lambda n: 1 if n == 1 else n * a_factaral(n - 1)

# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert a_factaral(0) == 1, "Zero"
    assert a_factaral(1) == 1, "One"
    assert a_factaral(2) == 2, "Two"
    assert a_factaral(3) == 6, "Six"
