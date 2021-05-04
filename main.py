'''
Executer le programme avec n le nombre de points voulu
'''
from Programme import trace_graphe as g, lier_points as lp
import sys
if '__main__' == __name__:
    n = int(sys.argv[-1])
    x,y = g.creer_pt(n)
    coord = lp.coord_pt(x,y)
    lp.tracer_liens(coord)
