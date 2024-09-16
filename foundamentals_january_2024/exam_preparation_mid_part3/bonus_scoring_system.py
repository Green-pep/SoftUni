number_of_students = int(input())
number_of_lectures = int(input())
bonus_of_the_course = int(input())

calculated_bonus = []
attendance_list = []
for student in range(number_of_students):
    attendance = int(input())
    attendance_list.append(attendance)
    total_bonus = attendance / number_of_lectures * (5 + bonus_of_the_course)
    calculated_bonus.append(total_bonus)

max_attendance = calculated_bonus.index(max(calculated_bonus))
print(f"Max Bonus: {round(max(calculated_bonus))}.")
print(f"The student has attended {attendance_list[max_attendance]} lectures.")
