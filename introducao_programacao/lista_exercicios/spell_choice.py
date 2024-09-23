class SpellChoice:
    def __init__(self, choice):
        self.choice = choice

    def display_spell(self):
        match self.choice:
            case 1:
                return "fire"
            case 2:
                return "water"
            case 3:
                return "earth"
            case _:
                return "Invalid choice"

if __name__ == "__main__":
    spell = SpellChoice(2)
    print(f"Chosen spell: {spell.display_spell()}")