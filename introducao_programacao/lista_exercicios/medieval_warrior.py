class MetalAlloy:
    def __init__(self, iron_kg, gold_kg):
        self.iron_kg = iron_kg
        self.gold_kg = gold_kg

    def is_iron_percentage_sufficient(self):
        total = self.iron_kg + self.gold_kg
        iron_percentage = (self.iron_kg / total) * 100
        return iron_percentage >= 70
if __name__ == "__main__":
    alloy = MetalAlloy(7, 3)
    print("Is iron percentage sufficient?", alloy.is_iron_percentage_sufficient())
