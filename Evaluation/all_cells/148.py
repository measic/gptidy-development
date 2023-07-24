# This cell does some preparatory work to run this Jupyter notebook using 
# IBM Data Science Experience (datascience.ibm.com). All the other cells remain the same as in the original example. 

# --------------------------------------------------------------------------------------------------
# IMPORTANT NOTES: 
# 1) Log on to your QX account and get your API token. You can get it from the Accounts page 
# (the top-right icon on QX website) Copy-Paste the API token below.BE SURE TO ENCLOSE IN QUOTES ("")
# 2) If you are sharing this notebook, MAKE SURE TO REMOVE the API token string before sharing! 
#   Alternatively, you can modify the code below and separately create and save Qconfig.py file with 
#   API token.
# --------------------------------------------------------------------------------------------------
QX_API_TOKEN = "PUT_YOUR_API_TOKEN_HERE"

import sys
import os

try:
    assert(sys.version_info.major > 2)
except AssertionError:          
    print("This code requires Python 3.5 or beyond. Your version: {}.{}".format(sys.version_info.major,sys.version_info.minor))
    raise

# DO NOT CHANGE THE FOLLOWING assertion
try:
    assert(QX_API_TOKEN != "PUT_YOUR_API_TOKEN_HERE")
except AssertionError:
    print("Update the value of QX_API_TOKEN first!")
    raise
    
# importlib.reload is used to reload the Qconfig module. Fixes any update problems with Qconfig.APItoken 
import importlib

# We need visibility to Qconfig.py module add current dir your sys.path
sys.path.append("./")

# Install qiskit package
!pip install qiskit
!rm -rf Qconfig.py 
!touch Qconfig.py

apitoken_str = 'APItoken=\"{}\"'.format(QX_API_TOKEN)
config_str = "config = { \"url\": 'https://quantumexperience.ng.bluemix.net/api'}"

with open('Qconfig.py', 'w') as fil:
    fil.write(apitoken_str + "\n")
    fil.write(config_str + "\n")
    
# Now import all the modules from qiskit such as QuantumProgram, QuantumCircuit, QuantumRegister etc.
# Optionally, you can modify the qiskit import line below to do specific module imports. 
from qiskit import *
import Qconfig

try:
    # Reload Qconfig module again to make sure the APItoken is updated
    importlib.reload(Qconfig)
except NameError as e:
    print("Name error: ", e.args)
except:
    print("unable to reload the module, continuing the execution..")
    
print("Qconfig.APItoken = ", Qconfig.APItoken)