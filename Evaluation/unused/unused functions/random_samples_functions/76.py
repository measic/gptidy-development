import pandas as pd 
import numpy as np

data_ep = pd.read_csv('data/exoplanet.eu_catalog.csv', 
                      usecols=['mass','mass_error_min','mass_error_max',
                               'semi_major_axis','semi_major_axis_error_min','semi_major_axis_error_max','star_name'])

class System:
    def __init__(self, data):
        self.data=data
        self.system = list(self.data.groupby("star_name").groups.keys())
        self.Number()
        self.Mass()
        self.CenterOfMass()
        #self.Error_CM()
        
    def Number(self):
        sys = self.data.groupby("star_name")
        self.N_total = len(sys["mass"])
        
    def Mass(self):
        sys = self.data.groupby("star_name")
        self.M_total = sys["mass"].sum()
    
    def CenterOfMass(self):
        self.rm_i = self.data["mass"].multiply(self.data["semi_major_axis"])
        self.data_i = self.data.assign(CM_i = self.rm_i.values) 
        p_system = self.data_i.groupby("star_name")
        sum_rm = p_system['CM_i'].sum()#.tolist()
        self.CM = sum_rm.divide(self.M_total)   
    
    def Error_CM(self):
        Sm2 = (self.data["mass_error_min"].multiply(self.data["mass_error_min"]))
        Sr2 = (self.data["semi_major_axis_error_min"].multiply(self.data["semi_major_axis_error_min"]))
        self.E_rm_i=np.sqrt(Sm2.divide(Sr2)+Sm2.divide(Sr2))