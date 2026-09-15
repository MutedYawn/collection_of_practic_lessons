ask_name = input("Вкажіть ваше ім'я\n:> ").capitalize()
ask_city = input("Вкажіть ваше місто\n:> ").capitalize()

def greet (ask_name, ask_city):
    print(f"Доброго дня, {ask_name} з міста {ask_city}!")
    return

greet(ask_name, ask_city)