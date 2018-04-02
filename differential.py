from sympy import *
from sympy import plot
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
    p = plot(eval(expressao),show=False,axis=True,autoscale=True,aspect_ratio=(1.0,1.0),title="MathBot",legend=True)
    file = 'graph.png'
    p.save(file)


def delete_graph(file):
    os.system('rm graph.png'.format(file))
