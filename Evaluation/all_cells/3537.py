# Reload when code changed:
%load_ext autoreload
%autoreload 2
%pwd
import os 
import sys
path = "../"
sys.path.append(path)
#os.path.abspath("../")
print(os.path.abspath(path))