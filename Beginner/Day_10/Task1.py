def is_leap_year(year):
    """checking if a year is leap year"""
    if year < 0:
        return print("Sorry, year shouldn't be negative")
    elif year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap = 2004
if is_leap_year(is_leap):
    print("This year is leap")
else:
    print("This year is not leap")
