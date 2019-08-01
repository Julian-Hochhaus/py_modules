#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from modules.tab2latex.tab2latex import textable
from modules.plot import axislabel as axis
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
import numpy as np
import math as math

#example textable
arr2= unp.uarray([1.09553e-12, 2,3,0], [0.0112445e-21, 0.0024400,0.20,0])
arr1=[2e12,3e-12,4.098346,5]
textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title columnÜ"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,3])
# dec_points sets precision, i.e. dec_points[0]=2 will display 2 decimal places for all values in column 1
# for values with uncertainties, the given value in dec_points is ignored. Instead, it follows the rounding rules defined by the Particle Data Group.



#example axislabel
x = np.linspace(-2, 2, 100)
plt.plot(x, x**2, 'b-', label="test")
axis.labels()#Note: function needs to be called in every plt instance!
plt.savefig('axislabel1.pdf')
plt.clf()

x = np.linspace(-3, 3, 100)
plt.plot(x, x**3, 'b-', label="test")
axis.labels()#Note: function needs to be called in every plt instance!
plt.savefig('axislabel2.pdf')
