class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        final_output = {"Name": self.name, "Guild": self.guild, "HP": self.hp, "MP": self.mp}
        player_details = "\n".join(f'{key}: {value}' for key, value in final_output.items())
        skills_details = "\n".join(f'==={key} - {value}' for key, value in self.skills.items())
        return player_details + "\n" + skills_details
