'''Function for creating a FP yield(A,Z) list container'''

def get_fpy_az( df ):
    '''
    Create a list of named tuple nuclides
    Parameters
    ----------
    df: pandas data frame, required
        Table of data for nuclides.
    
    Returns
    -------
    nuclides: list(namedtuple)
        List of namedtuples. Names: name, element_name, Z, A, yield_percent.

    Examples
    --------
    '''
    
    nuclides = list()

    # design a container data structure
    from collections import namedtuple
    FPY = namedtuple('FPY', ['name','element_name','Z','A','yield_percent'])

    import pandas as pd

    # Use the Mendeleev python package (periodic table of elements)
    from mendeleev import element
    
    total_yield = 0.0 # sum total yield
    for row in df.itertuples(index=False):
        z = int(row[0])
        for j in range(1,len(row)-1):
            if row[j] < 1.e-10: # this will eliminate many zeros
                continue
            a_str = df.columns[j] # index column is not part of the columns
            symbol = element(z).symbol
            name = name=symbol+'-'+a_str
            element_name = element(z).name
            yield_value = row[j]
            total_yield += yield_value
            nuc = FPY( name=name, element_name=element_name, Z=z, A=int(a_str), yield_percent=yield_value )
        
            nuclides.append(nuc)
            
    print('Sum of yield values in data file = ',round(total_yield,2))
    return nuclides