import matplotlib.pyplot as mlt
import numpy as np

grades = np.random.randint(0,101, size=(5, 20))
avereges = np.round(np.mean(grades, axis=1))

names = ["Вадим", "Настя", "Влад", "Данило", "Максим"]
colors = ["Green", "Blue", "skyblue", "crimson", "pink"]

mlt.bar(names, avereges, color=colors)
mlt.show()