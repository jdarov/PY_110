def time_from_string(string):
    integer_times = string.split(':')
    return (int(integer_times[0])*60 + int(integer_times[1]))


def after_midnight(time_string):
    return (time_from_string(time_string) if time_from_string(time_string) < 1440 else 0)

def before_midnight(time_string):
    AFTER_MIDNIGHT = after_midnight(time_string)
    return (1440 - AFTER_MIDNIGHT if AFTER_MIDNIGHT > 0 else 0)

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True