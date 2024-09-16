hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrive = int(input())
minute_of_arrive = int(input())

difference_hours = hour_of_arrive - hour_of_exam
difference_minutes = minute_of_arrive - minute_of_exam

if hour_of_arrive > hour_of_exam:
    print("Late")
    if hour_of_arrive >= hour_of_exam + 1 and difference_minutes >= 0:
        print(f'{difference_hours}:{difference_minutes:02d} hours after the start')
    else:
        difference_minutes = 60 - abs(difference_hours)
        print(f"{difference_minutes:02d} minutes after the start")
elif hour_of_arrive < hour_of_exam:
    if difference_hours <= 0 and -30 < difference_minutes <= 0:
        if difference_hours < 0:
            difference_minutes = 60 - difference_minutes
        print("Early")
        print(f"{difference_minutes:02d} minutes before the start")
    elif -30 >= difference_minutes <= 30 and difference_hours <= 0:
        print("On time")
        print(f"{difference_minutes} minutes before the start")


