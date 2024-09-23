class Weapon:
    def __init__(self, name, attack_power, durability):
        self.name = name
        self.attack_power = attack_power
        self.durability = durability

    def is_suitable(self):
        return self.attack_power > 50 and self.durability > 70

class FinalBattle:
    def __init__(self, weapons):
        self.weapons = weapons

    def choose_weapon(self):
        suitable_weapons = [weapon for weapon in self.weapons if weapon.is_suitable()]
        if suitable_weapons:
            return f"The most suitable weapon is: {suitable_weapons[0].name}"
        else:
            return "No suitable weapon. Seek a new one."

if __name__ == "__main__":
    weapons = [
        Weapon("Sword", 60, 80),
        Weapon("Bow", 40, 90),
        Weapon("Spear", 55, 60)
    ]
    battle = FinalBattle(weapons)
    print(battle.choose_weapon())
