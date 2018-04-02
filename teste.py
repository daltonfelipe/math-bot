from sympy import *
from sympy import plot
import os
import matplotlib
matplotlib.use('Agg')

x,y,z = symbols('x y z')

def graph(expressao,data):
    p = plot(eval(expressao),show=False,title="MathBot Graphs",legend=True)
    file = "%s"%data
    p.save(file)
    return file


def delete(file):
    os.system("rm {}".format(file))


g = graph('x**2','graph.png')
print(g)
#delete(g)
