class Vector:
    def __init__(self):
        self.vector = []

    def read_numbers(self):
        print("Enter 10 numbers:")
        for i in range(10):
            number = int(input(f"Number {i+1}: "))
            self.vector.append(number)

    def check_duplicates(self):
        duplicates = {}
        for i in range(len(self.vector)):
            number = self.vector[i]
            if self.vector.count(number) > 1:
                if number not in duplicates:
                    duplicates[number] = []
                duplicates[number].append(i)

        if duplicates:
            print("Duplicate numbers and their positions:")
            for number, positions in duplicates.items():
                print(f"Number {number} at positions: {positions}")
        else:
            print("No duplicate numbers in the vector.")

vector = Vector()
vector.read_numbers()
vector.check_duplicates()
