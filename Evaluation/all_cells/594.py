# Read in MCNP Simulated data
mcnpData = read_tally(mcnpPath+mcnpName,31, readGroups=True, splitTally=True)[1][1]
mcnpData.columns = [mcnpBinBounds, 'absFlux', 'relSigma']
mcnpData['absSigma'] = mcnpData['relSigma'] * mcnpData['absFlux']

tmpData1 = read_tally(mcnpPath+mcnpName,131, readGroups=True, splitTally=True)[0][1]

mcnpData['absFlux'] = mcnpData['absFlux'] + tmpData1['tally']
mcnpData['absSigma'] = np.sqrt(mcnpData['absSigma']**2 \
                                + (tmpData1['tally']*tmpData1['uncertainty'])**2)
mcnpData['relSigma'] = mcnpData['absSigma']/mcnpData['absFlux']

# Normalize the spectrum
mcnpData['normFlux'] = np.asarray(bin_differentiation(mcnpData[mcnpBinBounds].tolist(), 
                                 mcnpData['absFlux'].tolist(), mcnpBinBounds)) \
                                 * norm.mcnpNormFactor / norm.solidAngle \
                                 / norm.currentIntegrator/ (1-norm.deadTime)
mcnpData['normSigma'] = mcnpData['relSigma']*mcnpData['normFlux']
        
# Calculate the pdf and its uncertainty
mcnpData['pdfFlux'] = np.asarray(bin_differentiation(mcnpData[mcnpBinBounds].tolist(), 
                                  normAUBC(mcnpData['absFlux']).tolist(), mcnpBinBounds)) 
mcnpData['pdfSigma'] = mcnpData['relSigma']*mcnpData['pdfFlux']

# Build pdf histogram object
mcnpHisto=Histogram()
mcnpHisto.build_histo(mcnpData[mcnpBinBounds].tolist(), mcnpData['pdfFlux'].tolist(), 
                      uncert=mcnpData['pdfSigma'].tolist(), edgeLoc=mcnpBinBounds, name='MCNP')
mcnpHisto.plot(meuldersHisto, heprowHisto, heplogY=False, title='33MeV Deutrons on Ta',
                   xLabel='Energy [MeV]', yLabel='Neutron Intensity Energy Differential PDF', 
                   savePath=outPath+'33MeVTa_MCNP_pdf_lin_1_zoom')

# Build norm histogram object
mcnpNormHisto=Histogram()
mcnpNormHisto.build_histo(mcnpData[mcnpBinBounds].tolist(), mcnpData['normFlux'].tolist(), 
                          uncert=mcnpData['normSigma'].tolist(),edgeLoc=mcnpBinBounds,
                          name='MCNP')
mcnpNormHisto.plot(meuldersNormHisto, heprowNormHisto, heplogY=False, title='33MeV Deutrons on Ta',
                   xLabel='Energy [MeV]', yLabel='Neutron Intensity [n/MeV/uC/sr]', 
                   savePath=outPath+'33MeVTa_MCNP_norm_lin_1')