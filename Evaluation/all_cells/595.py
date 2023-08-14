# Log
heprowHisto.plot(meuldersHisto, logY=True, title='33MeV Deutrons on Ta Spectra',
                 xLabel='Energy [MeV]', yLabel='Neutron PDF',
                 savePath=outPath+'33MeVTa_pdf_log_1')
heprowNormHisto.plot(meuldersNormHisto, logY=True, title='33MeV Deutrons on Ta Spectra',
                 xLabel='Energy [MeV]', yLabel='Neutron Flux [n/MeV/uC/sr]',
                 savePath=outPath+'33MeVTa_norm_log_1')
heprowHisto.plot(logY=True, xLabel='Energy [MeV]', yLabel='Neutron Flux [n/MeV/uC/sr]',
                 savePath=outPath+'33MeVTa', legend=False)
#heprowCovErrorHisto.plot(heprowErrorHisto, nsdErrorHisto, logY=True, 
#                         title='16MeV Deutrons on Ta Spectra Errors',
#                         xLabel='Energy [MeV]', yLabel='Relative Error')

# Linear
heprowHisto.plot(meuldersHisto, title='33MeV Deutrons on Ta Spectra',
                 xLabel='Energy [MeV]', yLabel='Neutron PDF',
                 savePath=outPath+'33MeVTa_pdf_lin_1')
heprowNormHisto.plot(meuldersNormHisto, title='33MeV Deutrons on Ta Spectra',
                 xLabel='Energy [MeV]', yLabel='Neutron Intensity [n/MeV/uC/sr]',
                 savePath=outPath+'33MeVTa_norm_lin_1')