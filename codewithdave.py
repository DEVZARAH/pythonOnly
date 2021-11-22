"""
Dictionary
format ={'':''}

1. keys(), values(), items() method

2. get() method

setdefault()

to change a value
 variable[keys] = value

"""
"""
classes = {1: 'David', 2: 'Fatima', 3: 'Festus', 4: 'Solomon'}
print(classes.items())
print()
for name in classes.values():
    print(name)
print()
if 3 in classes:
    print(classes[3])"""

# shop = {'apples': 10, 'banana': 7, 'mangoes': 15, 'oranges': 87}

"""if 'banana' in shop:
    print(shop['banana'])
shop['apples'] = 50
print(shop)
print(shop.get('apples', 0))"""
"""
shop.setdefault('guava', 10)
print(shop)
import pprint
message = '_It was a bright cold day in april,  and clouds were pretty thick'

count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint.pprint(count)
"""

"""customers_response = input("Buyer: ")
print(f"Seller: How many {customers_response} do you want to buy?")
customers_response1 = int(input("Buyer: "))"""

"""shop = {'apples': 10,
        'banana': 20,
        'mangoes': 15,
        'oranges': 5
}
output = 0
if customers_response in shop:
    output = shop.get(customers_response, 0) * customers_response1
print(f"Seller: {customers_response1} {customers_response} will cost you ${output}")
print("Alright!")"""

shop = {'apples': 10,
        'banana': 20,
        'mangoes': 15,
        'oranges': 5
        }


def dialog():
    print("""
Seller: Hello, Welcome to Zahra store!
Buyer:  Thank you.
Seller: How may I help you
Buyer:  I love to buy some fruits
Seller: What fruits do you want to buy?
    """)


def customer(customer_response):
    if customer_response not in shop:
        return f"There are no {customer_response} available at the moment"

    else:
        print(f"Seller: How many {customers_response} do you want to buy?")
        customers_response1 = int(input("Buyer: "))
        cost = shop.get(customer_response, 0) * customers_response1
        return f"Seller: The {customer_response} will cost you ${cost}"


dialog()
customers_response = input("Buyer: ")
output = customer(customers_response)
print(output)