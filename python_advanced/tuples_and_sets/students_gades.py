number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    data = tuple(input().split())
    name, grade = data[0], float(data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)
for students, grade in students.items():
    print(f"{students} -> {' '.join(f'{i:.2f}' for i in grade)} (avg: {sum(grade)/len(grade):.2f})")
