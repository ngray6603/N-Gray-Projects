#establishing date
year = 0
month = 0
day = 0

year = int(input("Please enter a year from 2023-2099: "))
if year <2023 or year >2099:
    print("invalid year, please choose between 2023-2099.")
    return false
else:
    return true
month = int(input("Please enter a month from 1-12: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("Valid month with more than 30 days")
elif month == 4 or month ==6 or month == 9 or month == 11:
    print("Month with 30 days")
elif month == 2:
    print("Month only has 28 days")
else:
    print("Invalid Month")
#choosing correct day
day = int(input("please enter a day from 1-31"))

if month == 4 and day <= 30:
    print("Valid Day")

elif month == 6 and day <= 30:
    print("Valid Day")

elif month == 9 and day <=30:
    print("Valid Day")

elif month == 11 and day <= 30:
    print("Valid Day")

elif month == 2 and day <= 28:
    print("Valid Day")
else:
    print("That combination is not a valid day.")
