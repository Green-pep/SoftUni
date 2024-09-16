students_on_exam = int(input())

fail_evaluation = 0
low_success_rate = 0
better_success_rate = 0
good_success_rate = 0
counter_evaluation = 0

for student in range(students_on_exam):
    evaluation = float(input())
    counter_evaluation += evaluation
    if evaluation < 3:
        fail_evaluation += 1
    elif evaluation < 4:
        low_success_rate += 1
    elif evaluation < 5:
        better_success_rate += 1
    elif evaluation >= 5:
        good_success_rate += 1

average_evaluation = counter_evaluation / students_on_exam
fail_evaluation_percentages = fail_evaluation / students_on_exam * 100
low_success_rate_percentages = low_success_rate / students_on_exam * 100
better_success_rate_percentages = better_success_rate / students_on_exam * 100
good_success_rate_percentages = good_success_rate / students_on_exam * 100

print(f"Top students: {good_success_rate_percentages:.2f}%")
print(f"Between 4.00 and 4.99: {better_success_rate_percentages:.2f}%")
print(f"Between 3.00 and 3.99: {low_success_rate_percentages:.2f}%")
print(f"Fail: {fail_evaluation_percentages:.2f}%")
print(f"Average: {average_evaluation:.2f}")
