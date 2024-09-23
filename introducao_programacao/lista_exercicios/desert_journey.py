class DesertJourney:
    def __init__(self, water_available, distance_to_oasis):
        self.water_available = water_available
        self.distance_to_oasis = distance_to_oasis

    def is_water_sufficient(self):
        required_water = self.distance_to_oasis * 2
        return self.water_available >= required_water

if __name__ == "__main__":
    journey = DesertJourney(10, 4)
    print("Is water sufficient?", journey.is_water_sufficient())