def is_leap(year):
    leap = False
    if year % 4 == 0:
        if (year % 400 == 0 and year % 100 == 0) or (year % 400 != 0 and year % 100 != 0):
            leap = True
            return leap
        else:
            leap = False
            return leap
    else:
        return leap

    # Write your logic here


year = int(input())
print(is_leap(year))
