occurenceRegion = bigOccurences[8:15]
magnitudeRegion = bigMagnitudes[8:15]

parameters, covariance = curve_fit(expectedFit, magnitudeRegion, occurenceRegion)

fitX = magnitudeRegion

aFit = parameters[0]
bFit = parameters[1]

fitY = aFit * np.exp(-bFit * magnitudeRegion)

print("A = ", aFit, "b = ", bFit)