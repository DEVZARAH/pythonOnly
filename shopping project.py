shop = {
    "Apples": 10,
    "Banana": 5,
    "Grape": 25,
    "Orange": 13,
    "Pawpaw": 20,
    "Lime": 16
}

cart = {}


def compute_price(fruit, quantity):
    cost = shop.get(fruit, 0) * int(quantity)
    print(f"These {fruit} cost ${cost} at ${shop.get(fruit, 0)} each.")
    return cost


def update_cart():
    price = compute_price(fruit, quantities)
    cart.setdefault(fruit, price)
    return cart


def print_receipt():
    print(f"*******RECEIPT*******"
          f"ITEMS \t\t\t PRICES")
    total = 0
    for k, v in cart.items():
        print(f"{k}\t\t\t\t\t\t{v}")
        total += v
    print(f"The total price of your items is {total}")


while True:
    print("What fruits do you want to buy? ")
    fruit = input().title()
    if fruit in shop:
        print(f"How many {fruit} do you want to buy?: ")
        quantities = input()
        compute_price(fruit, quantities)
        update_cart()
        print("Press 1 to continue shopping or 2 to end shopping")
        response = int(input("> "))
        if response == 1:
            compute_price(fruit, quantities)
            update_cart()
        elif response == 2:
            print("Thanks for your patronage!")
            print(cart)
            break

    else:
        print(f"There are no {fruit} available in store at the moment. Thank you!")

print_receipt()