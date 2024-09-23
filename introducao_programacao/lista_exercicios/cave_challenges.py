class CaveChallenges:
    def __init__(self, door_number):
        self.door_number = door_number

    def show_challenge(self):
        match self.door_number:
            case 1:
                return "Fire Challenge"
            case 2:
                return "Water Challenge"
            case 3:
                return "Earth Challenge"
            case 4:
                return "Air Challenge"
            case 5:
                return "Darkness Challenge"
            case _:
                return "Invalid door number"

if __name__ == "__main__":
    cave = CaveChallenges(3)
    print(f"Challenge faced: {cave.show_challenge()}")
