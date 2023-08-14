# Import HEPROW, UNFANA, and Gravel data and normalize
heprowData = readGru(heprowPath+heprowName, delim_whitespace=True, names=[heprowBinBounds, 'absFlux', 'absSigma'],
               skiprows=3)
heprowData['absCovSigma'] = readMTX(heprowPath+mtxName).tolist()
heprowData['normFlux'] = np.asarray(bin_differentiation(heprowData[heprowBinBounds].tolist(), 
                                            heprowData['absFlux'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)
heprowData['normSigma'] = np.asarray(bin_differentiation(heprowData[heprowBinBounds].tolist(), 
                                            heprowData['absCovSigma'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)
        
unfData = readGru(heprowPath+unfanaName, delim_whitespace=True, 
                  names=[heprowBinBounds, 'absFlux', 'absSigma'], skiprows=3)
unfData['absCovSigma'] = readMTX(heprowPath+mtxName).tolist()
unfData['normFlux'] = np.asarray(bin_differentiation(unfData[heprowBinBounds].tolist(), 
                                            unfData['absFlux'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)
unfData['normSigma'] = np.asarray(bin_differentiation(unfData[heprowBinBounds].tolist(), 
                                            unfData['absCovSigma'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)    
        
grvData = readFlu(heprowPath+gravelName, delim_whitespace=True, 
                  names=[heprowBinBounds, 'absFlux', 'absSigma'], skiprows=3)
grvData['absCovSigma'] = readMTX(heprowPath+mtxName).tolist()
grvData['normFlux'] = np.asarray(bin_differentiation(grvData[heprowBinBounds].tolist(), 
                                            grvData['absFlux'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)
grvData['normSigma'] = np.asarray(bin_differentiation(grvData[heprowBinBounds].tolist(), 
                                            grvData['absCovSigma'].tolist(), heprowBinBounds)) \
                                            / norm.currentIntegrator / norm.solidAngle \
                                            / (1-norm.deadTime)

# Calculate the pdf and its uncertainty
heprowData['pdfFlux'] = normAUBC(heprowData['absFlux'])
heprowData['pdfSigma'] = heprowData['absSigma']/heprowData['absFlux']*heprowData['pdfFlux']
heprowData['pdfCovSigma'] = heprowData['absCovSigma']/heprowData['absFlux']*heprowData['pdfFlux']

unfData['pdfFlux'] = normAUBC(unfData['absFlux'])
unfData['pdfSigma'] = unfData['absSigma']/unfData['absFlux']*unfData['pdfFlux']
unfData['pdfCovSigma'] = unfData['absCovSigma']/unfData['absFlux']*unfData['pdfFlux']

grvData['pdfFlux'] = normAUBC(grvData['absFlux'])
grvData['pdfSigma'] = grvData['absSigma']/grvData['absFlux']*grvData['pdfFlux']
grvData['pdfCovSigma'] = grvData['absCovSigma']/grvData['absFlux']*grvData['pdfFlux']

# Build pdf histogram object
heprowHisto = Histogram()
heprowHisto.build_histo(heprowData[heprowBinBounds].tolist(), heprowData['pdfFlux'].tolist(),
                       uncert=heprowData['pdfCovSigma'].tolist(), edgeLoc=heprowBinBounds,
                       name='HEPROW')
unfHisto = Histogram()
unfHisto.build_histo(unfData[heprowBinBounds].tolist(), unfData['pdfFlux'].tolist(),
                       uncert=unfData['pdfCovSigma'].tolist(), edgeLoc=heprowBinBounds,
                       name='UNFANA')
grvHisto = Histogram()
grvHisto.build_histo(grvData[heprowBinBounds].tolist(), grvData['pdfFlux'].tolist(),
                       uncert=grvData['pdfCovSigma'].tolist(), edgeLoc=heprowBinBounds,
                       name='Gravel')
heprowHisto.plot(grvHisto,logY=True, title='33MeV Deutrons on Ta', xLabel='Energy [MeV]',
                 yLabel='Neutron PDF')
heprowHisto.write(outPath+'Det0_HEPROW_1_pdf', includeUncert=True, edge=False)

# Build norm histogram object
heprowNormHisto = Histogram()
heprowNormHisto.build_histo(heprowData[heprowBinBounds].tolist(), heprowData['normFlux'].tolist(),
                       uncert=heprowData['normSigma'].tolist(), edgeLoc=heprowBinBounds,
                       name='HEPROW')
heprowNormHisto.write(outPath+'Det0_HEPROW_1_norm', includeUncert=True, edge=False)

# Build error histogram objects
heprowErrorHisto = Histogram()
heprowErrorHisto.build_histo(heprowData[heprowBinBounds].tolist(),
                               heprowData['pdfSigma']/heprowData['pdfFlux'].tolist(),
                               edgeLoc=heprowBinBounds, name='HEPROW Errors')
heprowCovErrorHisto = Histogram()
heprowCovErrorHisto.build_histo(heprowData[heprowBinBounds].tolist(),
                               heprowData['pdfCovSigma']/heprowData['pdfFlux'].tolist(),
                               edgeLoc=heprowBinBounds, name='HEPROW Covariance Errors')