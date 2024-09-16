from battle.project import Pokemon

class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: list = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        print_data = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            print_data.append(f"- {p.pokemon_details()}")
        return "\n".join(print_data)

