city = input()
sells = float(input())

commission = 0

if city == "Sofia":
    if 0 < sells <= 500:
        commission = sells * 0.05
    elif 500 < sells <= 1000:
        commission = sells * 0.07
    elif 1000 < sells <= 10000:
        commission = sells * 0.08
    elif sells > 10000:
        commission = sells * 0.12
elif city == "Varna":
    if 0 < sells <= 500:
        commission = sells * 0.045
    elif 500 < sells <= 1000:
        commission = sells * 0.075
    elif 1000 < sells <= 10000:
        commission = sells * 0.10
    elif sells > 10000:
        commission = sells * 0.13
elif city == "Plovdiv":
    if 0 < sells <= 500:
        commission = sells * 0.055
    elif 500 < sells <= 1000:
        commission = sells * 0.08
    elif 1000 < sells <= 10000:
        commission = sells * 0.12
    elif sells > 10000:
        commission = sells * 0.145
if (city == "Sofia" or city == "Plovdiv" or city == "Varna") and sells > 0:
    print(f'{commission:.2f}')
else:
    print("error")