shopping_list = {}
print("Меню")

def add_item (name, price):
    shopping_list[name] = price 

def total_price (shopping_list):
    for price in shopping_list:
        total = total + price
    return total

def show_items(shopping_list):
    return sum(shopping_list.values())

while True: 
    print("1. додати / 2. показати суму / 3. показати список")
    user_choice = (input(":> ")).lower()
    if user_choice == ["1", "додати"]: 
        name = input("введіть ім'я продукту \n :>P") 
        price = float(input("введіть ціну\n :>"))
        add_item(name, price)
        