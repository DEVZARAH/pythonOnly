store = {
    "Bag": 100,
    "Shoe": 150,
    "Dress": 200,
    "Jewelries": 250,
    "Tag": 50,
    "Make-up": 350,
    "Accessories": 30
}

shopping_cart = {}


def compute_price(orders, quantity):
    price = store.get(orders) * int(quantity)
    return price


def update_cart(orders, cost):
    sums = 0
    if orders in shopping_cart:
        sums += cost
        shopping_cart.setdefault(orders, sums)
    else:
        shopping_cart.setdefault(orders, cost)


def generate_receipt():
    print("""
*******CUSTOMER'S RECEIPT*******
    """)
    print("RECEIPT\t\t\t\tITEM")
    total = 0
    for k, v in shopping_cart.items():
        total += v
        print(f"""{k}\t\t{v}""")
    print(f"""TOTAL\t\t{total}""")


def my_order(orders):
    num_of_orders = input(f"How many {orders}s do you want to add to your cart?: ")
    cost = compute_price(orders, num_of_orders)
    print(f"These {orders}s cost ${cost} at ${store.get(orders, 0)} each")
    update_cart(orders, cost)


# global scope
name = input("Name Pls!: ")
print(f"Hi! {name}, good to have you in our store, we sell varieties of apparels.")

order = input("What would you love to buy?: ").title()
if order not in store:
    print(f"{order}s not currently available at the moment")
else:
    my_order(order)
    while True:
        response = input("Enter 1 to continue shopping or 2 to quit: ")
        if response == '1':
            order = input("What else would you love to add to your cart?: ").title()
            if order in store:
                my_order(order)
            else:
                print(f"{order}s not currently available at the moment")
                continue
        elif response == '2':
            print("Thanks for for stopping by, here is your purchase receipt.")
            generate_receipt()
            break
        else:
            print("invalid input")

print(shopping_cart)
