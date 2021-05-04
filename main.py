import lier_points as lp
import trace_graphe as g
if '__main__' == __name__:
    n = 15
    x,y = g.creer_pt(n)
    coord = lp.coord_pt(x,y)
    lp.algo(coord)
