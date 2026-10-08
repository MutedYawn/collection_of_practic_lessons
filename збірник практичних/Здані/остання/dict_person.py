person = {                        # створюємо словник
    "name": "Max",
    "age": "16",
    "city": "Ivano-Frankivsk",
    "hobby": "listening to music"
}

print(person["city"])              # Виписуємо тільки од

del person['hobby']                # Видаляємо ключ

person["age"] = 17                 #змінюємо значення
person["email"] = "mail@gmail.com" # добавляємо ключ та значення

print(person.keys()) 

print(person)
