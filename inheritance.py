# Base Class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.__health = health  # Encapsulated attribute

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage
        return f"{self.name} takes {damage} damage! Health now: {self.__health}"

# Subclass with Polymorphism
class TechHero(Superhero):
    def __init__(self, name, gadget, health):
        super().__init__(name, "Technology Manipulation", health)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} activates their {self.gadget} to control technology!"

    def hack_system(self):
        return f"{self.name} hacks into the enemy system using {self.gadget}!"

# Creating instances
hero1 = Superhero("SolarMan", "Solar Beam", 100)
hero2 = TechHero("CyberKnight", "Neural Interface", 120)

# Demonstrating behavior
print(hero1.use_power())
print(hero1.take_damage(30))
print(hero2.use_power())
print(hero2.hack_system())
print(hero2.get_health())
