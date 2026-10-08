import matplotlib.pyplot as mlt
import numpy as np

grades = np.random.randint(0,101, size=(5, 20)) 
avereges = np.round(np.mean(grades, axis=1)) 
names = ["Вадим", "Настя", "Влад", "Данило", "Максим"]


mlt.plot(names, avereges, label="Середня оцінка")
mlt.grid()
mlt.title("Лінійний графік середніх оцінок")
mlt.legend()
mlt.ylabel("Оцінки")
mlt.xlabel("Ім'я")
mlt.show() 