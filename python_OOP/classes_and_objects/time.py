class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self,hours: int, minutes: int, seconds: int):
        self.hours = hours
        self. minutes = minutes
        self. seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        if self.seconds > Time.max_seconds:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes > Time.max_minutes:
            self.hours += self.minutes // 60
            self.minutes %= 60
        if self.hours > Time.max_hours:
            self.hours %= 24
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)

print(time.next_second())