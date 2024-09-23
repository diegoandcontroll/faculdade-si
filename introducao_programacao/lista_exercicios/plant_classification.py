class PlantClassification:
    def __init__(self, height):
        self.height = height

    def classify(self):
        if self.height < 1:
            return "small"
        elif 1 <= self.height <= 3:
            return "medium"
        else:
            return "large"

if __name__ == "__main__":
    plant = PlantClassification(2.5)
    print(f"Plant classification: {plant.classify()}")