def loading_bar(number: int):
    percentage = '%'
    point = "."
    percentage_loading = (number // 10)
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% [{percentage_loading * percentage}{(10 - percentage_loading) * point}]")
        print(f"Still loading...")


load_number = int(input())
loading_bar(load_number)
