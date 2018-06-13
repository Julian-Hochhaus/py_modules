# py_modules
If you got a problem or suggestions to improve the scripts, please create an [issue in git](https://github.com/Julian-Hochhaus/py_modules/issues).

Import via:
    from modules.table import textable



Using **textable**:


    textable.latex_tab(data=[arr1,arr2],names=[r"title column 1",r"title column 2"], filename=r"example.tex",caption=r"Beautiful caption",label=r"important_label",dec_points=[2,0], tableformat=3.3)


Where data_array must be an array of arrays; names_array must be an array of strings, containing the column-names, filename has to be a string,too.

dec_points sets precision for each column. dec_points is ignored, if uncertainty-arrays are used as input. Instead, the rounding rules by Particle Data Group are used (as in uncertainties-package implemented)

tableformat sets global column-width with
    tableformat=a.b
where a defines the number of spaces before the decimal separator and b after the decimal separator

For an example, have a look at example.py

label must be a string.
**Btw: You do not need to add prefix "tab:".**


Using **axislabel**

Import via:
    from modules.plot import axislabel as axis

Calling the function:
    axis.labels()
Grabs the current axis ticks and uses the german decimal separator ',' instead of the '.'

For an example, have a look at example.py
**Needs to be called in every plt instance!**
