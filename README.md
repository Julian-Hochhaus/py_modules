# py_modules
If you got a problem or suggestions to improve the scripts, please create an [issue in git](https://github.com/Julian-Hochhaus/py_modules/issues).

As long as these modules are not implemented as modules, you need to copy the scripts in your current working directory.
Usage:

Import the scripts to your python scripts i.e. with:

    import scriptname as foo



Using **textable**:

After importing textable, it can be used as follows:

    textable.latex_tab(data_array,names_array,filename,caption,label)

Where data_array must be an array of arrays; names_array must be an array of strings, containing the column-names, filename has to be a string,too.
label has to be a string. **Please notice: You do not need to add prefix "tab:".** 
