"""
p - input: integer
    output: string 'hh:mm'

    explicit: take integer, return a new string based on this integer and 24 hour clock
    implicit: integer will always be whole number
        neg or post

e - print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

d - integers, strings

a - if num < 60:
    return num/100
    create string from addition
    0.35 = 00.35
    if hour == 24, then 00

"""




def time_of_day(time):
    MINUTES_IN_DAY = 60 * 24

    minutes = time % MINUTES_IN_DAY
    

    hours = minutes // 60
    minutes = minutes % 60

    print(hours)
    print(minutes)

    print(f'{hours*60}')
    print(f'{hours:02d}:{minutes:02d}')
    return f'{hours:02d}:{minutes:02d}'

# print(time_of_day(0) == "00:00")        # True
print(time_of_day(1437) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
print(time_of_day(-640) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True