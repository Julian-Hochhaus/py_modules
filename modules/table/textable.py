import uncertainties
import numpy as np
def latex_tab(data=[[1,2,3],[42,42,42]],names=["col1","col2"],filename="test.tex",caption="Caption",label="test", dec_points=[0,2]):
    try: #test, if names and data and dec_points array have different lenghts
        for i in range(len(data)-1):
            if not(len(names)==len(data) and len(dec_points)==len(data)):
                raise TypeError("data and names and dec_points must have same dimension! "+"len(data)= "+str(len(data))+"; len(names)= "+str(len(names)) +"; len(dec_points)= "+str(len(dec_points)))
    except TypeError: raise
    else:
        #appends em dashs to shorter data arrays
        len_data_arr=[]
        for i in range(len(data)):
            len_data_arr.append(len(data[i]))
        len_data_max=max(len_data_arr)
        for i in range(len(data)):
            if not len_data_max==len(data[i]):
                for j in range(len_data_max-len(data[i])):
                    data[i]=np.append(data[i],'-')
        #start writing table
        texfile = open(filename,"w")
        texfile.write("\\begin{table}\n");
        texfile.write(" \\caption{"+caption+"}\n");
        texfile.write(" \\label{tab:"+label+"}\n")
        texfile.write(" \\centering\n")
        texfile.write("\\sisetup{detect-all}\n")#setup columnwidth to fit best
        texfile.write(" \\begin{tabular}{")
        for col in data:
            texfile.write("S")
        texfile.write("}\n");
        texfile.write(" \\toprule \n    ");
        #writing column titles
        for i in range(len(names)-1):
            texfile.write("{"+names[i]+"}& ")
        texfile.write("{"+names[len(names)-1]+"}")
        texfile.write(" \\\\\n");

        texfile.write("     \\midrule\n");
        #writing data
        for i in range(len_data_max):
            texfile.write("     ")
            #writing all data except the last columns
            for j in range(len(data)-1):

                if isinstance(data[j][i],uncertainties.core.Variable):
                    data[j][i]=(str(data[j][i])).replace('+/-',' \pm ')
                    texfile.write('$\\num{'+ data[j][i]+'}$'+" & ")
                else:
                    if(data[j][i]=='-'):
                        texfile.write("$\\text{\\textbf{---}}$"+"&")
                    else:
                        texfile.write(("{:10.%df}"%dec_points[j]).format(data[j][i])+" & ")
            #writing last column, seperated to get \n at the end
            if isinstance(data[len(data)-1][i],uncertainties.core.Variable):
                data[len(data)-1][i]=(str(data[len(data)-1][i])).replace('+/-','\pm')
                texfile.write('$\\num{'+ data[len(data)-1][i]+'}$')
            else:
                if(data[len(data)-1][i]=='-'):
                    texfile.write("$\\text{\\textbf{---}}$")

                else:
                    texfile.write(("{:10.%df}"%dec_points[len(dec_points)-1]).format(data[len(data)-1][i]))
            texfile.write(" \\\\\n")
        texfile.write(" \\bottomrule\n");
        texfile.write(" \\end{tabular}\n");
        texfile.write("\\end{table}");
        texfile.close()

#if module is executed as script:
if __name__ == "__main__":
    arr1=[1,3,4]
    arr2=[0.8,12,234,42,1.28]
    import textable
    print("42 is the answer to life the universe and everything!")
    print("Running this module as script generates a sample table.tex")
    latex_tab([arr1,arr2],["col1","col2"],"table.tex",'caption','sample')
