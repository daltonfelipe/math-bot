#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from numpy import *

def math(expressao): 
    try:
        return eval(expressao)
    except Exception as error:
        return error