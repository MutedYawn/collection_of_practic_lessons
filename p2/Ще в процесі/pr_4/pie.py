import matplotlib.pyplot as mlt

subjects = ["програмування", "математика", "англійська", "інші придмети"]
time = [40, 30, 20, 10]

mlt.pie(time, labels=subjects, autopct="%1.1f%%")
mlt.savefig(fname="pie.png")
mlt.show()
