class DragonRace:
    def __init__(self, distance, time):
        self.distance = distance
        self.time = time

    def calculate_speed(self):
        return self.distance / self.time

class DragonRaceChampionship:
    def __init__(self, dragon1, dragon2):
        self.dragon1 = dragon1
        self.dragon2 = dragon2

    def compare_dragons(self):
        speed1 = self.dragon1.calculate_speed()
        speed2 = self.dragon2.calculate_speed()
        if speed1 > speed2:
            return "Dragon 1 is faster"
        elif speed2 > speed1:
            return "Dragon 2 is faster"
        else:
            return "Both have the same speed"

if __name__ == "__main__":
    dragon1 = DragonRace(100, 10)
    dragon2 = DragonRace(100, 12)
    championship = DragonRaceChampionship(dragon1, dragon2)
    print(championship.compare_dragons())
