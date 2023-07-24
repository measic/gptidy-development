'''Function to read the blank-spaced column data into a Pandas data frame (table)'''

def read_table(file_name):
    '''
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
    '''
    import pandas as pd
    
    df = pd.read_csv(file_name, skiprows=6, delim_whitespace=True)
    
    # to avoid frustrations, set explicitly the data types of each column
    for c in df.columns: 
        if c == 'Y(NO-DIM)':
            continue
        df = df.astype({c: float}, copy=False)

    # print(df.dtypes)
    return df