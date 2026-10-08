import matplotlib.pyplot as mlt
import numpy as np

grades = np.random.randint(0,101, size=(50))

mlt.hist(grades, bins=10, edgecolor="black")
mlt.title("Розпроділ балів з англійської мови")
mlt.ylabel("Інтервали балів")
mlt.xlabel("Кількість студентів")
mlt.show()