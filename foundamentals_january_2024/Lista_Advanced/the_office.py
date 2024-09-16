happiness = map(int, input().split())
generally_happy = int(input())

multiply_emp = list(map(lambda x: x * generally_happy, happiness))
happy_employers = list(filter(lambda f: f >= sum(multiply_emp) / len(multiply_emp), multiply_emp))

if len(happy_employers) >= len(multiply_emp) / 2:
    print(f"Score: {len(happy_employers)}/{len(multiply_emp)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employers)}/{len(multiply_emp)}. Employees are not happy!")