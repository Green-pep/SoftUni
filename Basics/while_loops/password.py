username = input()
password = input()
some_password = input()

while some_password != password:
    some_password = input()

print(f"Welcome {username}!")
