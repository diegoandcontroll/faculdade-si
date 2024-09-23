class CoinCounting:
    def __init__(self, one_real, fifty_cents, twenty_five_cents):
        self.one_real = one_real
        self.fifty_cents = fifty_cents
        self.twenty_five_cents = twenty_five_cents

    def calculate_total_value(self):
        total_value = (self.one_real * 1) + (self.fifty_cents * 0.50) + (self.twenty_five_cents * 0.25)
        return total_value

if __name__ == "__main__":
    coins = CoinCounting(5, 10, 20)
    print(f"Total value: R${coins.calculate_total_value():.2f}")
