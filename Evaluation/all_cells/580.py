# Initialize objects
gROOT.ProcessLine('SimulationManipulation sm("{}",0)'.format(rspPath))
gROOT.ProcessLine('HistogramOperations ops')
gROOT.ProcessLine('HistogramWriter writer;')
gROOT.ProcessLine('lightTables.setBirksParams(1.0,6.90)')

# Create the bin structures
rspEbins=np.arange(rspEmin,rspEmax,rspEwidth)
rspEbins=np.append(rspEbins,rspEmax)
#print rspEbins
rspLbins=np.arange(rspLmin,rspLmax,rspLwidth)
rspLbins=np.append(rspLbins,rspLmax)
#print rspLbins
gROOT.ProcessLine('const Int_t EBINS = {}; const Int_t LBINS = {};'.format(len(rspEbins)-1,len(rspLbins)-1))
gROOT.ProcessLine('Double_t eEdges[EBINS + 1] = {}{}{};'.format("{",", ".join(str(e) for e in rspEbins),"}"))
gROOT.ProcessLine('Double_t lEdges[LBINS + 1] = {}{}{};'.format("{",", ".join(str(e) for e in rspLbins),"}"))
gROOT.ProcessLine('axis1 = TAxis(EBINS,eEdges);')
gROOT.ProcessLine('axis2 = TAxis(LBINS,lEdges);')

# Create the Histogram and output file
#gROOT.ProcessLine('TH2* matrix1=sm.getNormalizedResponseMatrix(axis1,axis2,1)')
gROOT.ProcessLine('TH2* matrix1=sm.getNormalizedResponseMatrix(axis1,axis2)')
gROOT.ProcessLine('writer.ResponseToHEPROW(matrix1,"EJ309_resp_03_1")')

# Smear the Response Matrix and Create the .rsp File
for detNum, detName in detNames.iteritems():   
    params = CalibParams(calPath+calNames[detNum])

    gROOT.ProcessLine('TH2* smearMatrix{0} = ops.skewedGausSmearMatrix(matrix1, {1}, {2}, {3})'.format(detNum, params.alpha, params.beta, params.gamma))
    gROOT.ProcessLine('smearMatrix{0}->Draw("colz")'.format(detNum))
    gROOT.ProcessLine('writer.ResponseToHEPROW(smearMatrix{0},"{1}_smearedResp_03_1")'.format(detNum,detName))
    
    pause()