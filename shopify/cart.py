# Code a function that will calculate a cart total price,
# based on various items prices and conditional discounts based on items type and quantity.
from decimal import Decimal

class Item:
    def __init__(self, price):
        self.price = price

class CheckoutItem:
    def __init__(self, item, quantity, discount_per_item):
        self.item = item
        self.quantity = quantity
        self.discount_per_item = discount_per_item


    def get_final_price(self):
        return (self.item.price - self.discount_per_item) * self.quantity

class Cart:
    def __init__(self, checkout_items):
        self.checkout_items = checkout_items

    def get_total(self):
        total = Decimal(0)
        for item in self.checkout_items:
            total = total + item.get_final_price()
        return total

if __name__ == '__main__':
    item_1 = Item(Decimal(99.97))
    item_2 = Item(Decimal(0.99))

    ch_item1 = CheckoutItem(item_1, 2, Decimal(20))
    ch_item2 = CheckoutItem(item_2, 10, Decimal(0.10))

    cart = Cart([ch_item1, ch_item2])
    print(cart.get_total())
