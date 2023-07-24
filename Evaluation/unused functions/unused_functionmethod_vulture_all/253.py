'''Function for creating a nuclide container'''

def get_nuclides( df ):
    '''
    Create a dictionary of nuclide name key and named tuple value
    Parameters
    ----------
    df: pandas data frame, required
        Table of data for nuclides.
    
    Returns
    -------
    nuclides: dict(name:namedtuple)
        Dictionary of name key and namedtuple values. Tuple names: element_name, symbol, Z, A, radius, unc.

    Examples
    --------
    '''
    
    nuclides = dict()

    # design a container data structure
    from collections import namedtuple
    Nuclide = namedtuple('Nuclide', ['element_name','symbol','Z','A','half_life'])

    # fill in the list of containers
    misses = 0 # counter of nuclides without radius data
    a_max = 0  # maximum A number with radius data present
    z_max = 0  # maximum Z number with radius data present
    t_max = 0

    import pandas as pd
    
    # Use the Mendeleev python package (periodic table of elements)
    from mendeleev import element
    
    # if df has duplicates, this loop will take care of it
    for row in df.itertuples(index=False):

        a = int(row[0])
        symbol = row[1]
        z = int(row[2])
        t = row[4]
        if pd.isnull(t): # missing half-life
            misses += 1
            continue
        if t/3600/24/365 > 50e+6: # remove anything with more than 50 My
            continue

        a_max = max(a,a_max)
        z_max = max(z,z_max)
        
        name = symbol+'-'+str(a)
        t_max = max(t,t_max)
        nuc = Nuclide( element_name=element(z).name, symbol=symbol, Z=z, A=a, half_life=t )
        
        if name in nuclides.keys():
            half_life = nuclides[name].half_life
            if half_life == t:
                continue
            else:
                name = name+'m'
        
        nuclides[name]=nuc

    print('Number of nuclides with    t_1/2 data = ',len(nuclides))
    print('Number of nuclides without t_1/2 data = ',misses)
    print('')
    print('Max Z number with t_1/2 data = ',z_max)
    print('Max A number with t_1/2 data = ',a_max)
    print('t_1/2 [Ma] max = ',t_max/3600/24/365/1000000)
    
    return nuclides