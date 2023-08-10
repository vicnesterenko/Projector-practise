class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        if isinstance(other, Country):
            new_country = f"{self.name} {other.name}"
            new_population = self.population + other.population
            return Country(new_country, new_population)
        else:
            raise ValueError("Can only add Country objects together")

    def __str__(self):
        return f"Name: {self.name}, population: {self.population}"


if __name__ == "__main__":
    bosnia = Country("Bosnia", 10_000_000)
    herzegovina = Country("Herzegovina", 5_000_000)
    bosnia_herzegovina = bosnia + herzegovina
    print(bosnia_herzegovina)
