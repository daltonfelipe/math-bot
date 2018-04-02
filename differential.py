from sympy import *
from sympy import plot
import os
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


def create_graph(expressao,user):
    p = plot(eval(expressao),show=False,title="MathBot",legend=True)
    file = '%s_graph.png'%user
    p.save(file)
    return file


def delete_graph(file):
    os.system('rm {}'.format(file))
