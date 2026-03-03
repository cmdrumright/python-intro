shopping_cart_items = []


def average_price(cart_items):
    average = 0

    for item in cart_items:
        average += item.price

    average = average / len(cart_items)

    return average


average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {shopping_cart_items} dollars")
