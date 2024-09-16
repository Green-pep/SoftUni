open_tabs = int(input())
salary = int(input())

for checking in range(open_tabs):
    type_of_tab = input()
    if salary <= 0:
        break
    if type_of_tab == "Facebook":
        salary -= 150
    elif type_of_tab == "Instagram":
        salary -= 100
    elif type_of_tab == "Reddit":
        salary -= 50
    else:
        continue
if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)
