# Import PHS data and plot
faltwPHSData = readFlu(heprowPath+faltwPHSName, delim_whitespace=True, names=['lowE', 'absPHS', 'absSigma'],
               skiprows=3)
measPHSData = readFlu(heprowPath+measPHSName, delim_whitespace=True, names=['lowE', 'absPHS', 'absSigma'],
               skiprows=3)
faltwPHSHisto = Histogram()
faltwPHSHisto.build_histo(faltwPHSData['lowE'].tolist(), 
                         bin_differentiation(faltwPHSData['lowE'].tolist(),
                                             faltwPHSData['absPHS'].tolist()),
                       uncert=faltwPHSData['absSigma'].tolist(), edgeLoc=heprowBinBounds,
                       name='FALTW')
measPHSHisto = Histogram()
measPHSHisto.build_histo(measPHSData['lowE'].tolist(), 
                         bin_differentiation(measPHSData['lowE'].tolist(),
                                             measPHSData['absPHS'].tolist()),
                         uncert=measPHSData['absSigma'].tolist(), edgeLoc=heprowBinBounds,
                         name='Measured')
faltwPHSHisto.plot(measPHSHisto, logY=True, title='33MeV Deutrons on Ta', xLabel='Light Yield [MeVee]',
                 yLabel='Counts per MeVee')