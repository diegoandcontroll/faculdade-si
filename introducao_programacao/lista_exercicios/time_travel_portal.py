class TimeTravelPortal:
    def __init__(self, energy, coordinates, time_adjustment):
        self.energy = energy
        self.coordinates = coordinates
        self.time_adjustment = time_adjustment

    def can_activate(self):
        if self.energy < 80:
            return "Energy is below required level"
        elif not self.coordinates:
            return "Coordinates are incorrect"
        elif not self.time_adjustment:
            return "Time adjustment is incorrect"
        else:
            return "Portal can be activated"

if __name__ == "__main__":
    portal = TimeTravelPortal(85, True, True)
    print(portal.can_activate())
