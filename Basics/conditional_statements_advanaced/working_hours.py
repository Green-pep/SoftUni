hours = int(input())
day_of_week = input()

if 10 <= hours <= 18:
    if day_of_week == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday":
        print("open")
elif day_of_week == "Sunday":
    print("closed")