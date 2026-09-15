import csv

while True:
    print("\n1. Створити CSV-файл з початковими студентами.")
    print("2. Показати всіх студентів.")
    print("3. Додати нового студента.")
    print("4. Оновити оцінку студента.")
    print("5. Видалити студента.")
    print("6. Показати студентів з оцінкою вище 10.")
    print("7. Вийти.")
    print("--==-=-==-=-==--")
    choice = input(":>")

    if choice == "7":
        print("Виконано: Вихід. Відпочивайте!")
        break
    
    elif choice == "1":
        # СТВОРЕННЯ ФАЙЛУ З ПОЧАТКОВИМИ ДАНИМИ
        with open("students.csv", "w", encoding="utf-8", newline="") as file: # newline="" захищає від появи порожніх рядків у Windows
            writer = csv.writer(file)
            writer.writerow(["name", "age", "grade"])                          # Записуємо заголовки колонок (шапку таблиці)
            writer.writerows([                                                 # Записуємо одразу кілька початкових рядків
                ["Анна", "16", "10"],
                ["Іван", "17", "11"],
                ["Марія", "16", "12"],
                ["Тереза", "17", "12"],
                ["Влад", "16", "10"],
                ["Денис", "16", "12"]
            ])
        print("Файл students.csv успішно створено з початковими студентами!")

    elif choice == "2":
        # ПОКАЗ ВСІХ СТУДЕНТІВ
        with open("students.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)                                          # csv.reader перетворює кожен рядок тексту на зручний список елементів
            next(reader)                                                       # Пропускаємо перший рядок-шапку ("name,age,grade")
            
            print("\n--- СПИСОК СТУДЕНТІВ ---")
            for row in reader:
                # row[0] - ім'я, row[1] - вік, row[2] - оцінка
                print(f"{row[0]} — {row[1]} років, оцінка: {row[2]}")

    elif choice == "3":
        # ДОДАВАННЯ НОВОГО СТУДЕНТА
        name = input("Введіть ім'я студента: ").strip()
        age = input("Введіть вік студента: ").strip()
        grade_input = input("Введіть оцінку студента (1-12): ").strip()

        # ПЕРЕВІРКА ЛОГІКИ: ім'я не порожнє, а оцінка в межах від 1 до 12
        if name != "" and grade_input.isdigit() and 1 <= int(grade_input) <= 12:
            with open("students.csv", "a", encoding="utf-8", newline="") as file: # Режим "a" (Append) дописує в кінець файлу
                writer = csv.writer(file)
                writer.writerow([name, age, grade_input])                      # Додаємо один новий рядок
            print(f"Студента {name} успішно додано!")
        else:
            print("Помилка введення! Ім'я не повинно бути порожнім, а оцінка має бути цифрою від 1 до 12.")

    elif choice == "4":
        # ОНОВЛЕННЯ ОЦІНКИ СТУДЕНТА
        search_name = input("Введіть ім'я студента, якому треба змінити оцінку: ").strip()
        
        # 1. Зчитуємо всі дані з файлу в список, бо файл не можна редагувати посередині
        students_list = []
        found = False
        
        with open("students.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)                                              # Зберігаємо шапку окремо
            for row in reader:
                students_list.append(row)                                      # Закидаємо студентів у список
        
        # 2. Шукаємо студента за ім'ям та змінюємо оцінку
        for row in students_list:
            if row[0].lower() == search_name.lower():                          # Перевірка без урахування регістру (мала/велика літера)
                new_grade = input(f"Знайдено! Введіть нову оцінку для {row[0]} (1-12): ").strip()
                if new_grade.isdigit() and 1 <= int(new_grade) <= 12:
                    row[2] = new_grade                                         # Змінюємо оцінку в нашому списку
                    found = True
                break

        # 3. Перезаписуємо оновлені дані у файл
        if found:
            with open("students.csv", "w", encoding="utf-8", newline="") as file: # Режим "w" очищає файл для повного перезапису
                writer = csv.writer(file)
                writer.writerow(header)                                        # Повертаємо назад шапку таблиці
                writer.writerows(students_list)                                # Записуємо весь змінений список
            print("Оцінку успішно оновлено!")
        else:
            print("Студента не знайдено.")

    elif choice == "5":
        # ВИДАЛЕННЯ СТУДЕНТА
        delete_name = input("Введіть ім'я студента для видалення: ").strip()
        
        students_list = []
        header = []
        found = False
        
        # 1. Зчитуємо дані
        with open("students.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                # 2. Фільтруємо: якщо ім'я не збігається, додаємо в список. Якщо збігається — пропускаємо (видаляємо)
                if row[0].lower() == delete_name.lower():
                    found = True
                else:
                    students_list.append(row)
        
        # 3. Перезаписуємо файл оновленим списком (вже без видаленого студента)
        if found:
            with open("students.csv", "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(students_list)
            print(f"Студента {delete_name} успішно видалено.")
        else:
            print("Студента не знайдено.")

    elif choice == "6":
        # ФІЛЬТРАЦІЯ ОЦІНОК (ВИЩЕ 10, ТОБТО 11 ТА 12 БАЛІВ)
        with open("students.csv", "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            
            print("\n--- СТУДЕНТИ З ОЦІНКОЮ 11 ТА 12 ---")
            has_top_students = False
            for row in reader:
                if int(row[2]) > 10:                                           # Перетворюємо оцінку-текст на число через int() для порівняння
                    print(f"{row[0]} — оцінка: {row[2]}")
                    has_top_students = True
            
            if not has_top_students:
                print("Студентів з такими оцінками не знайдено.")



# ТЕОРІЯ ДЛЯ ЗАХИСТУ ЗАВДАННЯ (КОМЕНТАРІ В КІНЦІ КОДУ):
#
# 1. Що таке CSV-файл і навіщо вбудований модуль csv?
#    CSV (Comma Separated Values) — це звичайний текстовий файл, де табличні дані записані рядками, 
#    а стовпчики розділені комами. Модуль csv потрібен, щоб Python автоматично парсив (розбивав) 
#    ці текстові рядки на готові списки/елементи, позбавляючи нас потреби різати текст вручну через .split(",").
#
# 2. Чим csv.reader відрізняється від csv.DictReader (або writer від DictWriter)?
#    - csv.reader читає рядки як стандартні СПИСКИ, де доступ до даних йде за індексами (row[0], row[1]).
#    - csv.DictReader читає рядки як СЛОВНИКИ, де ключами є заголовки колонок (row["name"], row["grade"]), 
#      що робить код наочнішим при великій кількості стовпчиків.
#    Те саме стосується і writer (приймає список списків) та DictWriter (приймає список словників).
#
# 3. Для чого використовується параметр newline="" при відкритті файлів для роботи з CSV?
#    Різні операційні системи (Windows та Linux/MacOS) по-різному кодують символ перенесення рядка (\n чи \r\n). 
#    Параметр newline="" вимикає внутрішню "самодіяльність" Python щодо інтерпретації цих символів. 
#    Якщо його не вказати у Windows, модуль csv під час запису буде вставляти порожні рядки через один після кожного запису.
