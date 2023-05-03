def getDays(month: int, year: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return -1

month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))
days = getDays(month, year)
if days == -1:
    print("Invalid month.")
else:
    print(f"The number of days in {month}/{year} is {days}.")
