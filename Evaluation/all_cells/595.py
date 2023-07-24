# Read in Meulders data and normalize
meuldersData = pd.read_table(meuldersPath+meuldersName, delim_whitespace=True, 
                             names=['upE', 'absFlux'])
meuldersData['absFlux'] = bin_differentiation(meuldersData['upE'],meuldersData['absFlux'],
                                             edgeLoc=meuldersBinBounds)
meuldersData['pdfFlux'] = normAUBC(meuldersData['absFlux'])

# Build pdf histogram object
meuldersHisto=Histogram()
meuldersHisto.build_histo(meuldersData['upE'].tolist(), meuldersData['pdfFlux'].tolist(), 
                         edgeLoc=meuldersBinBounds, name='Meulders')

# Build norm histogram object
meuldersNormHisto=Histogram()
meuldersNormHisto.build_histo(meuldersData['upE'].tolist(), meuldersData['absFlux'].tolist(), 
                         edgeLoc=meuldersBinBounds, name='Meulders')
meuldersNormHisto.plot(logY=True, title='33MeV Deutrons on Ta', xLabel='Energy [MeV]',
                 yLabel='Neutron Intensity [n/MeV/uC/sr]')