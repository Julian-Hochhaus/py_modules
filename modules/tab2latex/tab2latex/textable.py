import uncertainties
import numpy as np
import os
from uncertainties import ufloat

#######
#private functions
#######
def __write_seperator_or_newline(data,texfile,j):
    if(j==(len(data)-1)):
        texfile.write("\\")
    else:
        texfile.write("&")
#*********
#Write tables body
#*********

def __writedata(data,names,texfile,caption,label, dec_points,len_data_max):
            for i in range(len_data_max):
                texfile.write("     ")
                    #writing all data except the last columns
                for j in range(len(data)):
                    if isinstance(data[j][i],uncertainties.core.Variable) or (isinstance(data[j][i],uncertainties.core.AffineScalarFunc)):
                        if(str(data[j][i])=="0.0+/-0"):
                            texfile.write(r'{'+r'$\num{'+'0'+'}$'+r'}')
                            __write_seperator_or_newline(data,texfile,j);
                        else:
                            texfile.write(r'{'+r'${:L}$'.format(data[j][i])+r'}')
                            __write_seperator_or_newline(data,texfile,j);
                    else:
                        if(data[j][i]=='-'):
                            texfile.write(r'{'+r"$\\text{\\textbf{---}}$"+r'}')
                            __write_seperator_or_newline(data,texfile,j);
                        else:
                            val=ufloat(data[j][i],0)
                            val_str=r'{:L}'.format(val)
                            if('(' in val_str):
                                val,exp=val_str.split(r'\pm')
                                br,val=val.split('(')
                                val=str(round(float(val),dec_points[j]))
                                br,exp=exp.split(')')
                                texfile.write(r'{$'+val+exp+r'$}')
                            else:
                                val=str(round(val.n,dec_points[j]))
                                texfile.write(r'{$'+val+r'$}')

                            __write_seperator_or_newline(data,texfile,j);
                texfile.write(" \\\\\n")

#*********
#write dashes to shorter arrays
#*********

def __append_dashes_to_short_arrays(data, len_data_max):
    for i in range(len(data)):
        if not len_data_max==len(data[i]):
            for j in range(len_data_max-len(data[i])):
                data[i]=np.append(data[i],'-')

#*********
#returns max lenght of data arrays
#*********

def __max_array_lenght(data):
    len_data_arr=[]
    for i in range(len(data)):
        len_data_arr.append(len(data[i]))
    len_data_max=max(len_data_arr)
    return len_data_max

#*********
#write column heads
#*********

def __column_names(names,texfile):
    for i in range(len(names)-1):
        texfile.write("{"+names[i]+"}& ")
    texfile.write("{"+names[len(names)-1]+"}\\\ \n")

#*********
#write format string
#*********

def __write_format_string(data,format_string,texfile):
    if format_string==None:
        for col in data:
            texfile.write("S")
    else:
        texfile.write(format_string)
    texfile.write("}\n");

###############
#*********
#Error function
#*********

def __test_error(data,dec_points,names):
    for i in range(len(data)-1):
        if not(len(names)==len(data) and len(dec_points)==len(data)):
            raise TypeError("data and names and dec_points must have same dimension! "+"len(data)= "+str(len(data))+"; len(names)= "+str(len(names)) +"; len(dec_points)= "+str(len(dec_points)))

#######
#private functions
########
#*******
######


def long_tab(data=[[1,2,3],[42,42,42]],names=["col1","col2"],filename="test.tex",caption="Caption",label="test", dec_points=[0,2],format_string=None):
    try: #test, if names and data and dec_points array have different lenghts
        __test_error(data,dec_points,names)
    except TypeError: raise
    else:
        data=np.copy(data)
        #appends em dashs to shorter data arrays
        len_data_max=__max_array_lenght(data)
        __append_dashes_to_short_arrays(data,len_data_max)
        #start writing table
        texfile = open(filename,"w")
        texfile.write(" \\begin{longtable}{")
        __write_format_string(data,format_string,texfile);
        texfile.write(" \\caption{"+caption+"}\n");
        texfile.write("\\sisetup{detect-all, parse-numbers=false}\n")#setup columnwidth to fit best
        texfile.write(" \\label{tab:"+label+"}\\\ \n")
        texfile.write(" \\toprule"+"\n");
        __column_names(names,texfile)
        texfile.write("\\midrule\n");
        texfile.write("\\endfirsthead"+"\n")
        texfile.write(" \\toprule"+"\n");
        #writing column titles
        __column_names(names,texfile)
        texfile.write("\\midrule\n");
        texfile.write("\\endhead"+"\n")
        texfile.write("\\midrule\n");
        texfile.write("\\endfoot")
        texfile.write(" \\bottomrule\n");
        texfile.write("\\endlastfoot");
        __writedata(data,names,texfile,caption,label, dec_points,len_data_max)
        texfile.write(" \\end{longtable}\n");
        texfile.close()
############################################
####
def test():
	print("test")

####
############################################

def latex_tab(data=[[1,2,3],[42,42,42]],names=["col1","col2"],filename="test.tex",caption="Caption",label="test", dec_points=[0,2], format_string=None):
    try: #test, if names and data and dec_points array have different lenghts
        __test_error(data,dec_points,names)
    except TypeError: raise
    else:
        data=np.copy(data)
        #appends em dashs to shorter data arrays
        len_data_max=__max_array_lenght(data)
        __append_dashes_to_short_arrays(data,len_data_max)
        #start writing table
        texfile = open(filename,"w")
        texfile.write("\\begin{table}\n");
        texfile.write(" \\caption{"+caption+"}\n");
        texfile.write(" \\label{tab:"+label+"}\n")
        texfile.write(" \\centering\n")
        texfile.write("\\sisetup{detect-all, parse-numbers=false}\n")#setup columnwidth to fit best
        texfile.write(" \\begin{tabular}{")
        __write_format_string(data,format_string,texfile)
        texfile.write(" \\toprule \n    ");
        #writing column titles
        __column_names(names,texfile)
        texfile.write("     \\midrule\n");
        #writing data
        __writedata(data,names,texfile,caption,label, dec_points,len_data_max)
        texfile.write(" \\bottomrule\n");
        texfile.write(" \\end{tabular}\n");
        texfile.write("\\end{table}");
        texfile.close()

#if module is executed as script:
if __name__ == "__main__":
    arr1=[1e-30,0.0003,4]
    arr2=[0.8e-3,12234783573e12,234,42,1.2800000200]
    import textable
    print("42 is the answer to life the universe and everything!")
    print("Running this module as script generates a sample table.tex")
    latex_tab([arr1,arr2],["col1","col2"],"table.tex",'caption','sample')
