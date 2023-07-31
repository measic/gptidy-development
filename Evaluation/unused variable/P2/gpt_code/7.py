# Create the mfusg headfile object
headfile = os.path.join(modelpth, '{0}.hds'.format(modelname))
headobj = flopy.utils.HeadFile(headfile)
times = headobj.get_times()
_ = headobj.get_data(totim=times[-1])