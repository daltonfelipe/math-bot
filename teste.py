from sympy import *
from sympy import plot
import matplotlib
matplotlib.use('Agg')

x,y,z = symbols('x y z')

def dx(expressao):
    cmd = ('diff({})'.format(expressao)) 
    try:
        return eval(cmd)
    except Exception as error:
        return error

def integ(expressao):
    cmd = ('integrate({})'.format(expressao)) 
    try:
        return eval(cmd)
    except Exception as error:
        return error


def graph(expressao):
    p = plot(eval(expressao),show=False,title="MathBot Graphs",legend=True)
    p.save('graph.png')

graph('x**2')

