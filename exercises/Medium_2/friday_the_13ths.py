import datetime

def friday_the_13ths(year):
    friday_13ths = 0

    for month in range(1, 13):
        date = datetime.date(year, month, 13)
        if date.weekday() == 4:
            friday_13ths += 1
    return friday_13ths

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True