__author__ = 'KenMercusLai'
from datetime import timedelta
import datetime


def convert_to_second(time, unit):
    time = int(time)
    if 'minute' in unit:
        time *= 60
    elif 'hour' in unit:
        time *= 3600
    return time


def clock_pass_per_real_second(error_description):
    error_time, error_unit, _, pass_time, pass_unit = error_description.split()
    return convert_to_second(error_time, error_unit) * 1.0 / convert_to_second(pass_time, pass_unit) + 1


def time_to_int(time):
    hour, minute, second = map(int, time.split(':'))
    return hour * 3600 + minute * 60 + second


def get_real_time(start_time, pass_seconds):
    return (datetime.datetime.strptime(start_time, '%H:%M:%S') + timedelta(seconds=pass_seconds)).strftime('%H:%M:%S')


def broken_clock(starting_time, wrong_time, error_description):
    return get_real_time(starting_time,
                         (time_to_int(wrong_time) - time_to_int(starting_time)) / clock_pass_per_real_second(
                             error_description))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
