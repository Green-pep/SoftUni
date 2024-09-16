def password_validator(password):
    import re
    total_digits = len(re.findall('[0-9]', password))
    error_message = []
    password_range_requirement = range(6, 11)
    if len(password) not in password_range_requirement:
        error_message.append(f"Password must be between 6 and 10 characters")
    if not password.isalnum():
        error_message.append("Password must consist only of letters and digits")
    if total_digits < 2:
        error_message.append("Password must have at least 2 digits")
    if len(error_message) == 0:
        print("Password is valid")
    print(*error_message, sep="\n")



password_input = input()
password_validator(password_input)