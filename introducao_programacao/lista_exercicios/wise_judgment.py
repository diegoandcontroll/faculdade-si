class DuelJudgment:
    def __init__(self, attack1, defense1, attack2, defense2):
        self.attack1 = attack1
        self.defense1 = defense1
        self.attack2 = attack2
        self.defense2 = defense2

    def determine_winner(self):
        score1 = self.attack1 + self.defense1
        score2 = self.attack2 + self.defense2
        if score1 > score2:
            return "Warrior 1 is the winner"
        elif score2 > score1:
            return "Warrior 2 is the winner"
        elif self.defense1 > self.defense2:
            return "Warrior 1 wins due to higher defense"
        elif self.defense2 > self.defense1:
            return "Warrior 2 wins due to higher defense"
        else:
            return "It's a tie"

if __name__ == "__main__":
    duel = DuelJudgment(80, 70, 75, 75)
    print(duel.determine_winner())
