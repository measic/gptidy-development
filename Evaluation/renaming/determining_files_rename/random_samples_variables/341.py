def expectedFit(x, a, b):
    """
    Returns the expected fit for the histogram
    
    Arguments: x - the x value in the equation
               a - the first fit parameter
               b - the second fit paramter
               
    Returned: The expected fit function
    """
    return a * np.exp(-b * x)
occurenceRegion = bigOccurences[7:14]
magnitudeRegion = bigMagnitudes[7:14]
parameters, variable_def = curve_fit(expectedFit, magnitudeRegion, occurenceRegion)
fitX = magnitudeRegion
aFit = parameters[0]
bFit = parameters[1]
fitY = aFit * np.exp(-bFit * magnitudeRegion)
print('A = ', aFit, 'b = ', bFit)