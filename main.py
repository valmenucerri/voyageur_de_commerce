'''
Executer le programme avec n le nombre de points voulu
'''
from Programme import trace_graphe as g, lier_points as lp
import sys
from Programme_graphe_incomplet import tracer_lien_2 as lp2,traiter_graphe as gr
if '__main__' == __name__:
    '''n = int(sys.argv[-1])
    x,y = g.creer_pt(n)
    coord = lp.coord_pt(x,y)
    lp.tracer_liens(coord)
    '''
    graphe = gr.recup_fichier(sys.argv)
    N = gr.nbr_noeud(graphe)
    L = gr.analyser_graphe(graphe,N)
    parcours = lp2.parcourir_graphe(L,N)
