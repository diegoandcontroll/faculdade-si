class BonusCalculator:
    def __init__(self, missions_completed):
        self.missions_completed = missions_completed

    def calculate_bonus(self):
        if self.missions_completed > 10:
            return 100
        elif 5 <= self.missions_completed <= 10:
            return 50
        else:
            return 10

if __name__ == "__main__":
    bonus = BonusCalculator(5)
    print(f"Bonus amount: {bonus.calculate_bonus()} gold coins")