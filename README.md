# py_modules
If you got a problem or suggestions to improve the scripts, please create an [issue in git](https://github.com/Julian-Hochhaus/py_modules/issues).

Import via:
    from modules.table import textable



Using **textable**:


    textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title column 2"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,0])

Where data_array must be an array of arrays; names_array must be an array of strings, containing the column-names, filename has to be a string,too.
dec_points sets precision for each column.
For an example, have a look at example.py
label has to be a string. **Please notice: You do not need to add prefix "tab:".** 
