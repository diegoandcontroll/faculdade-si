class AnimalGuessing:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def suggest_animal(self):
        if self.animal_type == 'mammal':
            return "dog"
        elif self.animal_type == 'reptile':
            return "turtle"
        else:
            return "Unknown animal type"

if __name__ == "__main__":
    guessing = AnimalGuessing('mammal')
    print(f"Suggested animal: {guessing.suggest_animal()}")
