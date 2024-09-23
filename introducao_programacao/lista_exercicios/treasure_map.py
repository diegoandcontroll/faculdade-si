class TreasureMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self):
        return self.x + self.y
if __name__ == "__main__":
    n1 = int(input("Enter first step: "));
    n2 = int(input("Enter first step: "));
    treasure = TreasureMap(n1, n2)
    print(f"Total distance: {treasure.calculate_distance()} steps")
