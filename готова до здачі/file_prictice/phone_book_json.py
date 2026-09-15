import json

# Перевіряємо, чи існує файл, якщо ні — створюємо його порожнім списком, щоб програма не падала на старті
try:
    with open("phone_book.json", "r", encoding="utf-8") as file:
        json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    with open("phone_book.json", "w", encoding="utf-8") as file:
        json.dump([], file, ensure_ascii=False, indent=4)

while True:
    print("\n1. Створити телефонну книгу (початкові контакти)")
    print("2. Показати всі контакти")
    print("3. Додати контакт")
    print("4. Знайти контакт за іменем")
    print("5. Оновити номер телефону")
    print("6. Видалити контакт")
    print("7. Вийти")
    print("==-=-==--==-=-==")
    choice = input("Оберіть дію: \n:> ")

    if choice == "7":
        print("Виконано: Вихід з програми. Гарного відпочинку!")
        break

    elif choice == "1":
        # СТВОРЕННЯ КНИГИ (ЗАПИС ПОЧАТКОВИХ КОНТАКТІВ)
        initial_contacts = [
            {"name": "Анна", "phone": "+380501112233", "city": "Львів"},
            {"name": "Іван", "phone": "+380674445566", "city": "Київ"},
            {"name": "Марія", "phone": "+380937778899", "city": "Одеса"}
        ]
        with open("phone_book.json", "w", encoding="utf-8") as file:
            json.dump(initial_contacts, file, ensure_ascii=False, indent=4)     # json.dump() перетворює Python-структуру на текст JSON і пише у файл
        print("Телефонну книгу успішно створено з початковими контактами!")

    elif choice == "2":
        # ПОКАЗ ВСІХ КОНТАКТІВ
        with open("phone_book.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)                                         # json.load() зчитує JSON-файл і перетворює його назад у Python-список словників
            
        if not contacts:
            print("Телефонна книга порожня.")
        else:
            print("\n--- ВСІ КОНТАКТИ ---")
            for person in contacts:
                print(f"{person['name']} — {person['phone']}, місто: {person['city']}")

    elif choice == "3":
        # ДОДАВАННЯ КОНТАКТУ
        # 1. Завантажуємо поточний список
        with open("phone_book.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)

        # 2. Запитуємо нові дані
        name = input("Введіть ім'я: ").strip()
        phone = input("Введіть телефон: ").strip()
        city = input("Введіть місто: ").strip()

        if name and phone and city:
            new_contact = {"name": name, "phone": phone, "city": city}
            contacts.append(new_contact)                                       # Додаємо новий словник у наш список через .append()

            # 3. Зберігаємо оновлений список назад у файл
            with open("phone_book.json", "w", encoding="utf-8") as file:
                json.dump(contacts, file, ensure_ascii=False, indent=4)
            print(f"Контакт {name} успішно додано!")
        else:
            print("Помилка: Всі поля мають бути заповнені!")

    elif choice == "4":
        # ПОШУК ЗА ІМЕНЕМ
        search_name = input("Введіть ім'я для пошуку: ").strip()
        
        with open("phone_book.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)

        found = False
        for person in contacts:
            if person["name"].lower() == search_name.lower():                  # Пошук без урахування регістру літер
                print(f"Знайдено: {person['name']} — {person['phone']}, місто: {person['city']}")
                found = True
                break
        
        if not found:
            print("Контакту з таким іменем не знайдено.")

    elif choice == "5":
        # ОНОВЛЕННЯ НОМЕРА ТЕЛЕФОНУ
        search_name = input("Введіть ім'я контакту, номер якого хочете змінити: ").strip()

        # Чому вантажимо все в Python? Бо файл JSON — це цілісний рядок тексту, не можна змінити один шматок прямо на диску!
        with open("phone_book.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)

        found = False
        for person in contacts:
            if person["name"].lower() == search_name.lower():
                new_phone = input(f"Введіть новий номер для {person['name']}: ").strip()
                person["phone"] = new_phone                                    # Змінюємо значення ключа у словнику
                found = True
                break

        if found:
            with open("phone_book.json", "w", encoding="utf-8") as file:
                json.dump(contacts, file, ensure_ascii=False, indent=4)        # Записуємо змінену структуру назад
            print("Номер телефону успішно оновлено!")
        else:
            print("Контакту не знайдено.")

    elif choice == "6":
        # ВИДАЛЕННЯ КОНТАКТУ
        search_name = input("Введіть ім'я для видалення контакту: ").strip()

        with open("phone_book.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)

        # Фільтруємо список: залишаємо тільки тих, чиє ім'я НЕ збігається з пошуком
        updated_contacts = [p for p in contacts if p["name"].lower() != search_name.lower()]

        if len(contacts) != len(updated_contacts):                             # Якщо довжина змінилася — значить когось видалили
            with open("phone_book.json", "w", encoding="utf-8") as file:
                json.dump(updated_contacts, file, ensure_ascii=False, indent=4)
            print(f"Контакт {search_name} успішно видалено.")
        else:
            print("Контакту не знайдено.")


# ====================================================================================================
# ТЕОРІЯ ДЛЯ ЗАХИСТУ ЗАВДАННЯ (КОМЕНТАРІ В КІНЦІ КОДУ):
#
# 1. Що таке JSON і чим він відрізняється від звичайного тексту?
#    JSON (JavaScript Object Notation) — це загальноприйнятий текстовий формат обміну даними. Від звичайного 
#    тексту він відрізняється суворою структурою (в основі лежать пари "ключ: значення" та масиви). Python 
#    розуміє його і легко перетворює на свої рідні списки (list) та словники (dict).
#
# 2. Що робить функція json.dump(), а що — json.load()?
#    - json.dump() — бере об'єкт Python (наприклад, список словників) і перетворює його на формат JSON, 
#      записуючи цей результат у файл (Serialization).
#    - json.load() — зчитує структурований текст із файлу JSON і конвертує його назад у зрозумілі об'єкти Python 
#      (Deserialization).
#
# 3. Для чого потрібні параметри ensure_ascii=False та indent=4 при записі JSON?
#    - ensure_ascii=False — змушує Python записувати символи національних алфавітів (кирилицю, українські "і", "є", "ї") 
#      як нормальні літери, а не кодувати їх у вигляді екранованих послідовностей на кшталт "\u0410".
#    - indent=4 — задає відступи (у цьому випадку 4 пробіли) для оформлення тексту у файлі. Без нього весь JSON 
#      запишеться в один нечитабельний довгий рядок, а з ним він стає красивим і структурованим для людини.
#
# 4. Чому для оновлення JSON-файлу потрібно спочатку повністю завантажити його вміст у Python, змінити і записати назад?
#    JSON-файл зберігається на жорсткому диску як один суцільний послідовний рядок символів. Фізично неможливо 
#    вставити або видалити шматок тексту всередину файлу без руйнування його структури. Тому єдиний правильний 
#    шлях: прочитати весь файл в оперативну пам'ять (у об'єкти Python), виконати будь-які маніпуляції (додати/видалити/змінити) 
#    і повністю перезаписати файл з нуля новою структурою.
# ====================================================================================================