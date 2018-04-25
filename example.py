from modules.table import textable

#example textable
arr1=[0.4,0.75,1.4]
arr2=[2,3,4]
textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title column 2"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,0])
# dec_points sets precision, i.e. dec_points[0]=2 will display 2 decimal places for all values in column 1 
