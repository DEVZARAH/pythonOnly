shop = {
    "apples": 10,
    "Banana": 5,
    "Grape": 25,
    "Orange": 13,
    "Pawpaw": 20,
    "Lime": 16
}


'''def dialogue(name):
    print(f"""
    {name}: Hello, I am {name}
    Tony:    Hello {name}, Welcome to Zahra Fruit Store!
    {name}:  Thank you.
    Tony:    How may I help you?
    {name}: I would love to buy some fruits
    Tony:    What fruits do you want to buy?
        """)
'''

def shopping(fruit, name):
        if fruit in shop:
            print(f"How many {fruit} do you want to buy")
            quantity = input(f"{name}: ")
            cost = shop.get(fruit, fruit) * int(quantity)
            return f"{name}! These {fruit} cost ${cost}"

        else:
            return f"There are no {fruit} available in store at the moment" \
                   f"Thank you!"


print("seller: Hi! I am Tony, you are? ")
name = input("> ")
dialogue(name)
fruits = input(f"{name}: ")
output = shopping(fruits, name)
print(output)


''''def dialogue(name):
    print(f"""
    {name}: Hello, I am {name}
    Tony:    Hello {name}, Welcome to Zahra Fruit Store!
    {name}:  Thank you.
    Tony:    How may I help you?
    {name}: I would love to buy some fruits
    Tony:    What fruits do you want to buy?
        """)


def shopping(fruit, name):
    fruits_list = fruit.split()
    cost = ""
    for fruit_list in shop:
        print(f"How many {fruit} do you want to buy")
        quantity = input(f"{name}: ")
        cost += shop.get(fruit_list, fruit) * int(quantity)
        return f"{name}! These {fruit} cost ${cost}"

    else:
        return f"There are no {fruit} available in store at the moment" \
               f"Thank you!"


print("seller: Hi! I am Tony, you are? ")
name = input("> ")
dialogue(name)

fruits = input(f"{name}: ")
output = shopping(fruits, name)
print(output)
'''
