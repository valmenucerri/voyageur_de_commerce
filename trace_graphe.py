import random as rd
import matplotlib.pyplot as plt
import lier_points as lp
n = 30
x = [ rd.random() for _ in range(n) ]
y = [ rd.random() for _ in range(n) ]

plt.plot(x,y,"o")
print(x,y)
lp.coord_pt(x,y)
