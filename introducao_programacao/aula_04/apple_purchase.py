class ApplePurchase:
    NORMAL_PRICE_PER_APPLE = 1.30
    DISCOUNTED_PRICE_PER_APPLE = 1.00
    DISCOUNT_THRESHOLD = 12

    def __init__(self, number_of_apples):
        self.number_of_apples = number_of_apples

    def calculate_total_cost(self):
        if self.number_of_apples >= ApplePurchase.DISCOUNT_THRESHOLD:
            price = ApplePurchase.DISCOUNTED_PRICE_PER_APPLE
        else:
            price = ApplePurchase.NORMAL_PRICE_PER_APPLE
        
        return self.number_of_apples * price


if __name__ == "__main__":
    quantity = int(input("Enter the number of apples purchased: "))
    purchase = ApplePurchase(quantity)
    total_cost = purchase.calculate_total_cost()
    print(f"The total cost of the purchase is R$ {total_cost:.2f}")