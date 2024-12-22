class Discount:
    def calculate(self, price, discount_type):
        if discount_type == "seasonal":
            return price * 0.9
        elif discount_type == "clearance":
            return price * 0.5


class Discount:
    def calculate(self, price):
        return price

class SeasonalDiscount(Discount):
    def calculate(self, price):
        return price * 0.9

class ClearanceDiscount(Discount):
    def calculate(self, price):
        return price * 0.5
