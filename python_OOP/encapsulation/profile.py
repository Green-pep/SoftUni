class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_long_enough = len(value) > 7
        is_upper_password = len([el for el in value if el.isupper()]) > 0
        is_digit_password = len([el for el in value if el.isdigit()]) > 0
        if not is_long_enough or not is_upper_password or not is_digit_password:
            raise ValueError("The password must be 8 or more characters with "
                             "at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)