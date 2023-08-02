#Set name of MODFLOW exe
#  assumes executable is in users path statement
exe_name = 'mfusg'
if platform.system() == 'Windows':
    exe_name += '.exe'
mfexe = exe_name

modelpth = os.path.join('data')
modelname = 'zaidel'

#make sure modelpth directory exists
if not os.path.exists(modelpth):
    os.makedirs(modelpth)