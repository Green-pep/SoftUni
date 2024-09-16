n = int(input())

found = False

for a in range(1, 10):
    for b in range(a, -1, -1):  # b се движи от a до 0
        for c in range(10):
            for d in range(c, -1, -1):  # d се движи от c до 0
                sum_of_digits = a + b + c + d
                product_of_digits = a * b * c * d

                # Проверка на първото условие
                if sum_of_digits == product_of_digits and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    found = True
                    break

                # Проверка на второто условие
                if product_of_digits != 0 and product_of_digits % sum_of_digits == 0 and product_of_digits // sum_of_digits == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    found = True
                    break

                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("Nothing found")
