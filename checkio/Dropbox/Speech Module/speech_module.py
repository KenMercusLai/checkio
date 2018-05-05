FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number_string = ''
    if number >= 0 and number <= 999:
        hundreds = number // 100
        if hundreds > 0:
            number_string = (number_string
                             + FIRST_TEN[hundreds - 1]
                             + ' ' + HUNDRED + ' ')
        number = number - hundreds * 100
        if number >= 20 and number <= 99:
            number_string += OTHER_TENS[number // 10 - 2] + ' '
            number = number - (number // 10) * 10
        if number > 0:
            if number >= 10 and number <= 19:
                number_string += SECOND_TEN[number % 10] + ' '
                number = number - 10
            elif number >= 0 and number <= 9:
                number_string += FIRST_TEN[number - 1]
    return number_string.strip()


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(
        ' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
