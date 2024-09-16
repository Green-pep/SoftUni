student_name = input()
good_evaluation = 0
bad_evaluation = 0
grade = 0
average_evaluation = 0

while grade < 12:
    evaluation_grade = float(input())
    if evaluation_grade < 4:
        bad_evaluation += 1
        if bad_evaluation > 1:
            excluded_year = grade + 1
            print(f"{student_name} has been excluded at {excluded_year} grade")
            break
        continue

    elif evaluation_grade >= 4:
        grade += 1
        good_evaluation += evaluation_grade
        average_evaluation = good_evaluation / grade
        if grade == 12:
            print(f"{student_name} graduated. Average grade: {average_evaluation:.2f}")


