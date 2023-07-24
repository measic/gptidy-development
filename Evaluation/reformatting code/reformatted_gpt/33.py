def pre_process(table, dream9):
    # Select all variables that are not categorical
    tables = [table[[v for v in table.keys() if v not in categorical]]]

    # Convert yes/no to 1/0
    alias_dict = {'SEX': {'F': 1}, 'PRIOR.MAL': {'YES': 1}, 'PRIOR.CHEMO': {'YES': 1}, 'PRIOR.XRT': {'YES': 1},
                  'Infection': {'Yes': 1}, 'ITD': {'POS': 1, 'ND': numpy.nan}, 'D835': {'POS': 1, 'ND': numpy.nan},
                  'Ras.Stat': {'POS': 1, 'NotDone': numpy.nan}, 'resp.simple': {'CR': 1}, 'Relapse': {'Yes': 1},
                  'vital.status': {'A': 1}}

    tables += [alias(table, alias_dict)]

    # Split data that has multiple values
    tables += [split(table['cyto.cat'], dream9)]

    # Create new data for protein
    tables += [squared(table[protein])]
    tables += [absolute(table[protein])]
    tables += [bin_independent(table[protein], dream9, 2)]
    tables += [bin_independent(table[protein], dream9, 3)]
    tables += [bin_independent(table[protein], dream9, 4)]
    tables += [bin_independent(table[protein], dream9, 5)]

    # Make PCA axis
    tables += [make_pca(table[protein], dream9, 200, name='PCA')]
    tables += [make_pca(table[protein], dream9, 200, name='Whiten_PCA', whiten=True)]
    tables += [make_pca(squared(table[protein]), squared(dream9[protein]), 200, name='PCA_Sq')]

    # Bin dependent variables
    try:
        tables += [cutoff(table[['Overall_Survival', 'Remission_Duration']], 130)]
        tables += [binned(table[['Overall_Survival', 'Remission_Duration']])]
    except KeyError:
        pass

    # Join everything
    return pandas.concat(tables, axis=1)