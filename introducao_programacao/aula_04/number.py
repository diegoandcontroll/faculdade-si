class Number:
    def __init__(self, value):
        self.value = value

    def check_if_positive_or_negative(self):
        if self.value >= 0:
            return "The value is positive."
        else:
            return "The value is negative."


if __name__ == "__main__":
    value = float(input("Enter a numeric value (integer or real): "))
    number = Number(value)
    print(number.check_if_positive_or_negative())
