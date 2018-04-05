#!/usr/bin/env python
# -*- coding: utf-8 -*-
help_msgs = u"""
Ola, bem vindo ao MathBot vBeta... Utilize os seguintes comandos para utilizar corretamente o bot.

Comandos aceitáveis

/help - Exibe o menu ajuda

/math - Recebe uma expressão matemática e envia sua solução.
>>> Ex.: /math sin(1+1) - (seno de 1 + 1)
>>> /math_lista - lista das operações possiveis.

/integral - Calcula a integral de uma função.
>>> Ex.: /integral cos(2*x),x - (integral de cos(2x) em relação a x)

/dx - Calcula a derivada de uma uma função.
>>> Ex.: /dx x**2,x - (derivada de x**2 em relação a x)

/grafico - Gera um grafico bidimensional com a função desejada.
>>> Ex.: /grafico x**2

/grafico3d - Gera um grafico tridimensional com a função desejada.
>>> Ex.: /grafico3d x**2 + y**2

*  Os comandos aceitos são das libs numpy e sympy do  python2.7.
** Outros comandos serão ignorados e não terão resposta.
"""


math_lista = u'''

  Operações Básicas
   + -> soma
   - -> subtração
   / -> divisão
   * -> multiplicação

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
