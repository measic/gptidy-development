# analysis by identified risk factors for prevalent infection: 
# age group, deprivation index and lifetime number of sexual partners
factors = ['Age group', 'Deprivation', 'Age left school', 
           'Age at first heterosexual sex', 'Sexual partners, last year', 
          'New sexual parterns, last year', 'Sexual partners without a condom, last year',
          'Lifetime sexual partners', 'Condom use at most recent sex', 
          'Concurrent partnerships, last year', 'Binge drinking',
          'Same sex experience/contact, ever']

# proportion of those surveyed reporting each risk factor level
n3_props =[[0.373, 0.627],
           [0.369,0.182,0.449],
           [0.754, 0.246],
           [0.351, 0.261, 0.388],
           [0.573, 0.187, 0.136, 0.104],
           [0.421, 0.326, 0.253],
           [0.331, 0.475, 0.194],
           [0.527, 0.224, 0.249],
           [0.517, 0.483],
           [0.712, 0.143, 0.145],
           [0.526, 0.202, 0.273],
           [0.08, 0.92]]

# proportion reporting testing in the last year, by risk factor level
n3_test = [[0.404, 0.311],
           [0.345, 0.333, 0.352],
           [0.336, 0.378],
           [0.256, 0.334, 0.453],
           [0.26, 0.403, 0.43, 0.609],
           [0.26, 0.367, 0.463],
           [0.270, 0.343, 0.488],
           [0.253,0.396,0.492],
           [0.335, 0.38],
           [0.329, 0.497, 0.385],
           [0.281, 0.399, 0.432],
           [0.339, 0.424]] 

# proportion reporting diagnosis in the last year, by risk factor level
n3_diag = [[0.404*0.047, 0.311*0.067],
           [0.345*0.052, 0.333*0.05, 0.352*0.065],
           [0.336*0.053, 0.378*0.072],
           [0.256*0.028, 0.334*0.047, 0.453*0.078],
           [0.26*0.034, 0.403*0.009, 0.43*0.015, 0.609*0.212],
           [0.26*0.055, 0.367*0.04, 0.463*0.08],
           [0.270*0.018, 0.343*0.049, 0.488*0.109],
           [0.253*0.01,0.396*0.038,0.492*0.123],
           [0.335*0.043, 0.38*0.074],
           [0.329*0.067, 0.497*0.065, 0.385*0.013],
           [0.281*0.035, 0.399*0.04, 0.432*0.098],
           [0.339*0.058, 0.424*0.051]]