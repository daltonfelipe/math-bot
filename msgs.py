#!/usr/bin/env python
# -*- coding: utf-8 -*-
help_msgs = u"""
Ola, bem vindo ao MathBot vBeta... Utilize os seguintes comandos para utilizar corretamente o bot.

Comandos aceitáveis

/help - Exibe o menu ajuda.

/exemplos - Exibe um menu interativo com alguns exemplos.

/math - Recebe uma expressão matemática e envia sua solução.
>>> Ex.: /math sin(1+1) - (seno de 1 + 1).
>>> /math_lista - lista das operações possiveis.

/integral - Calcula a integral de uma função.
>>> Ex.: /integral cos(2*x),x - (integral de cos(2x) em relação a x)

/dx - Calcula a derivada de uma uma função.
>>> Ex.: /dx pow(x,2),x - (derivada de x^2 em relação a x).

/plot - Gera um gráfico bidimensional com a função desejada.
>>> Ex.: /plot pow(x,2)

/plot3d - Gera um gráfico tridimensional com a função desejada.
>>> Ex.: /plot3d pow(x,2)+pow(y,2)

*  Os comandos aceitos são das libs numpy e sympy do  python2.7.
** Outros comandos serão ignorados e não terão resposta.
"""


math_lista = u'''

  Operações Básicas
   + -> soma
   - -> subtração
   / -> divisão
   * -> multiplicação
   pow(2,2) -> 2 elevado a 2

  Funções Trigonométricas
   sin(x) -> seno(x)     / arcsin(x) -> arcosseno(x)
   cos(x) -> cosseno(x)  / arccos(x) -> arcocosseno(x)
   tan(x) -> tangente(x) / arctan(x) -> arcotangente(x)
   
  Constantes
   pi  -> pi
   e   -> euler

  Estatística
   mean([x1,x2,xn]) -> media
   std([x1,x2,xn])  -> desvio padrão	

'''
