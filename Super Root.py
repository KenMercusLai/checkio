def super_root(number):
    x = 0
    base = 1.0
    while not number - 0.001 < x ** x < number + 0.001:
        if x ** x <= number - 0.001:
            x += base
        else:
            base /= 2
            x -= base
    return x

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
