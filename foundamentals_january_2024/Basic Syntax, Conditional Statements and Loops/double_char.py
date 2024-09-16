string = ""
while string != "End":
    double_string = ""
    string = input()
    if string == "SoftUni" or string == "End":
        continue
    for char in string:
        double_string += char * 2
    print(double_string)
