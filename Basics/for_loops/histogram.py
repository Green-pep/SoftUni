n = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0


for _ in range(n):
    numbers = int(input())

    if numbers < 200:
        p1_counter += 1
    elif numbers < 400:
        p2_counter += 1
    elif numbers < 600:
        p3_counter += 1
    elif numbers < 800:
        p4_counter += 1
    else:
        p5_counter += 1

p1_percentages = (p1_counter / n) * 100
p2_percentages = (p2_counter / n) * 100
p3_percentages = (p3_counter / n) * 100
p4_percentages = (p4_counter / n) * 100
p5_percentages = (p5_counter / n) * 100

print(f"{p1_percentages:.2f}%")
print(f"{p2_percentages:.2f}%")
print(f"{p3_percentages:.2f}%")
print(f"{p4_percentages:.2f}%")
print(f"{p5_percentages:.2f}%")
