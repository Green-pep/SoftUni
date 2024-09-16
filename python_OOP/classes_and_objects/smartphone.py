class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps: list = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app, app_memory) -> str:
        if app_memory <= self.memory and not self.is_on:
            return f"Turn on your phone to install {app}"

        elif app_memory <= self.memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
