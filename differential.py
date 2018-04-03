from sympy import *
from sympy import plot
from sympy.plotting import plot3d
from sympy.abc import * 
import os
import matplotlib
matplotlib.use('Agg')

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


def create_graph(expressao):
    p = plot(eval(expressao),show=False,title="MathBot",legend=True)
    file = 'graph.png'
    p.save(file)

def create_graph3d(expressao):
    p = plot3d(eval(expressao),show=False,title="MathBot")
    file = 'graph.png'
    p.save(file)

def delete_graph(file):
    os.system('rm graph.png'.format(file))
