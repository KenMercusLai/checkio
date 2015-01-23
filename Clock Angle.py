def clock_angle(time):
    hour, minute = time.split(':')
    hour = int(hour) + int(minute) * 1.0 / 60
    if hour > 12:
        hour -= 12
    AngelHour = hour / 12 * 360
    AngelMinute = int(minute) / 60.0 * 360
    if AngelMinute > AngelHour:
        ClockAngle = round(abs(AngelMinute - AngelHour), 1)
    else:
        ClockAngle = round(abs(AngelHour - AngelMinute), 1)
    if ClockAngle <= 180:
        return ClockAngle
    else:
        return 360 - ClockAngle

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
