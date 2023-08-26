mf = flopy.modflow.Modflow(modelname=modelname, exe_name=mfexe, model_ws=modelpth)
dis = flopy.modflow.ModflowDis(mf, nlay, nrow, ncol, delr=delr, delc=delc, top=botm[0, :, :], botm=botm[1:, :, :], perlen=1, nstp=1, steady=True)
variable_def = flopy.modflow.ModflowBas(mf, ibound=ibound, strt=strt)
lpf = flopy.modflow.ModflowLpf(mf, hk=0.0001, laytyp=4)
oc = flopy.modflow.ModflowOc(mf, stress_period_data={(0, 0): ['print budget', 'print head', 'save head', 'save budget']})
sms = flopy.modflow.ModflowSms(mf, nonlinmeth=1, linmeth=1, numtrack=50, btol=1.1, breduc=0.7, reslim=0.0, theta=0.85, akappa=0.0001, gamma=0.0, amomentum=0.1, iacl=2, norder=0, level=5, north=7, iredsys=0, rrctol=0.0, idroptol=1, epsrn=1e-05, mxiter=500, hclose=0.001, hiclose=0.001, iter1=50)
mf.write_input()
try:
    os.remove(os.path.join(model_ws, '{0}.hds'.format(modelname)))
except:
    pass
mf.run_model()