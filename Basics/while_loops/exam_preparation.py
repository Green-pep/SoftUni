max_bad_grades = int(input())
bad_grades = 0
good_grades = 0
count_tasks = 0
last_task_name = ""
failed_tasks = False

while True:
    task_name = input()
    if task_name == "Enough":
        break
    grade = int(input())
    count_tasks += 1
    good_grades += grade
    last_task_name = task_name
    if grade <= 4:
        bad_grades += 1
        if bad_grades >= max_bad_grades:
            failed_tasks = True
            break

average_grade = good_grades / count_tasks
if failed_tasks:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_tasks}")
    print(f"Last problem: {last_task_name}")

