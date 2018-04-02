from sympy import *
from sympy import plot
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


def create_graph(expressao,data='math_bot'):
    p = plot(eval(expressao),show=False,title="MathBot",legend=True)
    user = data['from_user'].username
    user = 'felipe'
    file = '{}_graph.png'.format(user)
    p.save(file)
    return file


def delete_graph(file):
    os.system('rm {}'.format(file))    
