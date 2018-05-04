def sun_angle(time):
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)
    converted_time = (hour - 6) * 60 + minute
    if converted_time < 0 or converted_time > 12 * 60:
        return "I don't see the sun!"
    return round(converted_time / (12 * 60) * 180, 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
