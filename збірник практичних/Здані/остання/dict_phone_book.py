phone_book = { 
    "Тереза": "+380 123 456 789",
    "Денис": "+380 523 476 889",
    "Влад": "+380 567 443 231",
}

for name in phone_book:
        print("=-=-=-" *2)
        print(name)
        print("=-=-=-" *2)

choice = input("Вітаю, кому сьогодні дзвонимо? \n :>").capitalize()

while True:
    if choice in phone_book:
        print(f'гаразд дзвонимо {choice} {phone_book[choice]}')
        print("=-=-=-" *2) 
        x = input("Дзвонемо ще комусь?").lower()
        if x in ["ні", "н"]:
             break
        else:
            choice = input("Кому щедзвонимо?\n:>").capitalize()

    else:
        print('Контакт не знайдено')
        x = input("Дзвонемо ще комусь?").lower()
        if x in ["ні", "н"]:
             break
        else:
            choice = input("Кому щедзвонимо?\n:>").capitalize()