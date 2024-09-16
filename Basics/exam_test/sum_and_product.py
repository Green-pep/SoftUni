n = int(input())
combination = 0
is_found_abcd = False

for a in range(0, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, -1):
                if a + b + c + d == a * b * c * d and n % 5 == 0:
                    is_found_abcd = True
                    print(f"{a}{b}{c}{d}")
                elif a * b * c * d // a + b + c + d == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                else:
                    print("Nothing found")#Ако разделим произведението (a * b * c * d) на сумата (a + b + c + d) и получим 3 (целочислено), и едновременно с това n се дели на 3 без остатък, трябва да се принтира числото dcba.)



