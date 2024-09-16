import math
figure_type = str(input())

if figure_type == "square":
    a = float(input())
    square_area = a ** 2
    print(f'{square_area:.3f}')
if figure_type == "rectangle":
    a = float(input())
    b = float(input())
    rectangle_area = a * b
    print(f'{rectangle_area:.3f}')
if figure_type == "circle":
    a = float(input())
    circle_area = math.pi * (a ** 2)
    print(f'{circle_area:.3f}')
if figure_type == "triangle":
    a = float(input())
    b = float(input())
    triangle_area = (a * b) / 2
    print(f'{triangle_area:.3f}')