def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    # Format a number as friendly text, using common suffixes.
    greaterThan0 = number >= 0
    number = abs(number)
    for i in range(len(powers)):
        if number / base ** i < base:
            break
    value = number / base ** i

    if decimals:
        format_string = '{0:0<.%df}{1}{2}' % (decimals)
        value = format_string.format(value, powers[i], suffix)
    else:
        format_string = '{0}{1}{2}'
        value = format_string.format(int(value), powers[i], suffix)

    if greaterThan0:
        return value
    else:
        return '-' + value


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(
        1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
