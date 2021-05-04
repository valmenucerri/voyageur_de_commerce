import random as rd
import matplotlib.pyplot as plt
import lier_points as lp
n = 30
def creer_pt(n):
    x = [ rd.random() for _ in range(n) ]
    y = [ rd.random() for _ in range(n) ]
    plt.scatter(x, y)
    return x,y




