from modules.table import textable
import uncertainties.unumpy as unp
#example textable
arr2= unp.uarray([1.095473487583, 2,3], [0.0112445, 0.002,0.2])
arr1=[2,3,4]
textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title column 2"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,0], tableformat=3.3)
# dec_points sets precision, i.e. dec_points[0]=2 will display 2 decimal places for all values in column 1
# for values with uncertainties, the given value in dec_points is ignored. Instead, it follows the rounding rules defined by the Particle Data Group.  
#tableformat sets global column-width 
