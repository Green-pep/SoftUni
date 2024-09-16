def start_rhombus(size):
    for star in range(1, n + 1):
        white_space = " " * (n - star)
        stars = "* " * star
        print(f"{white_space}{stars}")
    for star in range(n - 1, 0, -1):
        white_space = " " * (n - star)
        stars = "* " * star
        print(f"{white_space}{stars}")


n = int(input())
start_rhombus(n)