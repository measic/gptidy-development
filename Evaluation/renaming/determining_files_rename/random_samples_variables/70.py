"""Function to read the blank-spaced column data into a Pandas data frame (table)"""

def read_table(file_name):
    """
    Read table data into a `pandas` data frame (table).  
    
    Parameters
    ----------
    file_name: str, required
        File name and its path relative to this notebook.
    
    Returns
    -------
    df: pandas.df
        `Pandas` data frame (table).

    Examples
    --------
    """
    import pandas as pd
    variable_def = pd.read_csv(file_name, skiprows=6, delim_whitespace=True)
    for c in variable_def.columns:
        if c == 'Y(NO-DIM)':
            continue
        variable_def = variable_def.astype({c: float}, copy=False)
    return variable_def