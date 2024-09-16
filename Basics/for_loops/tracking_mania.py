group_climbers = int(input())

musala_counter = 0
monblan_counter = 0
kilimandjaro_counter = 0
k2_counter = 0
everest_counter = 0

all_members = 0

for group_climbers in range(group_climbers):
    members = int(input())
    all_members += members

    if members <= 5:
        musala_counter += members
    elif members <= 12:
        monblan_counter += members
    elif members <= 25:
        kilimandjaro_counter += members
    elif members <= 40:
        k2_counter += members
    else:
        everest_counter += members

musala_percentages = (musala_counter / all_members) * 100
monblan_percentages = (monblan_counter / all_members) * 100
kilimandjaro_percentages = (kilimandjaro_counter / all_members) * 100
k2_percentages = (k2_counter / all_members) * 100
everest_percentages = (everest_counter / all_members) * 100

print(f"{musala_percentages:.2f}%")
print(f"{monblan_percentages:.2f}%")
print(f"{kilimandjaro_percentages:.2f}%")
print(f"{k2_percentages:.2f}%")
print(f"{everest_percentages:.2f}%")
