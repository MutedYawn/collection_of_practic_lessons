def len_check(user_password):
    if len(user_password) >= 8:
        return True                                                     # Повертає True, якщо довжина пароля 8 символів і більше
    else:
        return False                                                    # Повертає False, якщо пароль занадто короткий

def upper_check(user_password):
    for alpha in user_password:
        if alpha.isupper():
            return True                                                 # Повертає True при виявленні першої ж великої літери
    return False                                                        # Повертає False, якщо після перевірки всього рядка великих літер немає

def digit_check(user_password):
    for digit in user_password:
        if digit.isdigit():
            return True                                                 # Повертає True при виявленні першої ж цифри
    return False                                                        # Повертає False, якщо після перевірки всього рядка цифр немає

def clear_check(user_password):
    if len(user_password) == 0:
        return True                                                     # Повертає True, якщо користувач нічого не ввів
    else:
        return False                                                    # Повертає False, якщо рядок містить хоча б один символ

def check_password(user_password):
    if clear_check(user_password) == True:
        print("Пароль слабкий: порожній!")
        return                                                          # Зупиняє подальші перевірки, якщо пароль пустий
    
    if len_check(user_password) == False:
        print("Пароль слабкий: занадто короткий!")
        return                                                          # Зупиняє перевірки, якщо довжина менша за 8
    
    if upper_check(user_password) == False:
        print("Пароль слабкий: не містить велику літеру!")
        return                                                          # Зупиняє перевірки, якщо немає великих літер
    
    if digit_check(user_password) == False:
        print("Пароль слабкий: не містить цифру!")
        return                                                          # Зупиняє перевірки, якщо немає цифр
    
    print("Пароль надійний")                                            # Спрацьовує, якщо всі попередні перевірки повернули True

while True:  
    user_password = input("Введіть ваш пароль: ")
    check_password(user_password)                                       # Виклик головної функції валідації для введенного пароля
    print("+-" * 20)

# ТЕОРІЯ:
# 1. Функція-валідатор це функція, яка перевіряє дані на відповідність правилам (валідує їх).
# 2. Вона повертає True (якщо все ок) або False (якщо знайдено помилку), бо це логічний тип, зручний для перевірок.
# 3. Ділити задачу на функції круто, бо код стає чистішим, його легше читати, тестувати та змінювати в одному місці.