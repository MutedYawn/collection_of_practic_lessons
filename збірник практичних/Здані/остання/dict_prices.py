prices = {                             # Створення словника prices (5 товарів та їхні ціни)
    "apple": 20,
    'orange': 30,
    'strawberry': 40,
    'banana': 15,
    'cherry': 25
}

prices["grape"] = 20                   # Додавання нового товару до словника
prices["strawberry"] = 25              # Зміна ціни для існуючого товару (полуниці)
del prices["orange"]                   # Видалення одного товару (апельсина) за його ключем

# Знаходження найдорожчого товару через параметр key=prices.get (порівнює ціни, а не назви)
max_product = max(prices, key=prices.get)
max_price = prices[max_product]
print(f'Максимальна ціна у продукта {max_product}, ціна: {max_price} грн\n')

print("Доступні товари:")
for product, price in prices.items():  # Виведення всіх товарів та цін на екран у зрозумілому вигляді
    print(f"{product}:> {price} грн")
    print("=-=-")

while True:                            # Нескінченний цикл для пошуку товарів за запитом користувача
    Support = input("\nБудь ласка, введіть назву продукта > ").lower()
    
    if Support in prices:              #  оператор 'in' шукає ключ і повертає True/False
        print("Товар в наявності!")
        print(f'Ціна {Support} становить: {prices[Support]} грн')
    else:
        print('Товар не знайдено')

    choice = input("\nЩе щось? (так/ні) > ").lower()
    
    if choice in ["ні", "н", "n", "no"]: # Перевірка виходу з циклу за допомогою оператора 'in'
        print("До зустрічі! Бажаємо вам гарного дня!")
        break