def is_palindrome(number_as_string) -> bool:
    if number_as_string == number_as_string[::-1]:
        return True
    return False


numbers = input().split(", ")

for number in numbers:
    print(is_palindrome(number))

