from datetime import datetime


def date_time(time: str) -> str:
    converted_dt = datetime.strptime(time, "%d.%m.%Y %H:%M")
    preformated_date = converted_dt.strftime('{} %B %Y year')
    preformated_date = preformated_date.format(converted_dt.day)
    preformated_hour = '{} hour'.format(converted_dt.hour)
    if converted_dt.hour != 1:
        preformated_hour += 's'
    preformated_minute = '{} minute'.format(converted_dt.minute)
    if converted_dt.hour != 1:
        preformated_minute += 's'
    return ' '.join([preformated_date, preformated_hour, preformated_minute])


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
