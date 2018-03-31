from sympy import *

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


