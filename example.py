from modules.table import textable
from modules.plot import axislabel as axis
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
import numpy as np
print np.__version__
#example textable
arr2= unp.uarray([1.09553, 2,3], [0.0112445, 0.00244,0.2])
arr1=[2,3,5,6,7]
textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title column 2"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,0])
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
