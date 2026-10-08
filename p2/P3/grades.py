import numpy as np

grades = np.random.randint(0, 101, size=(100, 3)) #робимо список оцінок З ТРЬОХ ПРИДМЕТІВ
print(grades)

averages = np.round(np.mean(grades, axis=1)) #вираховуємо середній бал з ТРЬОХ придметів та закруглюємо їх.
print(averages)