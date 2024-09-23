class CastleDefense:
    def __init__(self, army_position):
        self.army_position = army_position

    def activate_defense(self):
        match self.army_position:
            case "inside":
                return "Defense system is off"
            case "outside":
                return "Defense system is on"
            case _:
                return "Invalid position"

if __name__ == "__main__":
    defense = CastleDefense("outside")
    print(defense.activate_defense())
