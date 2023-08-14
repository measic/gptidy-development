import numpy as np
import matplotlib.pyplot as plt
from sys import exit
import math

plt.close()

#-----------Part 1----------------

# Generating Training and Testing Data
# Creating a class for the dataset
class Data_set:
    def __init__(self, mean, cov):
        self.mean = mean
        self.cov  = cov
    
    def split_data(self):
        np.random.shuffle(self.data)
        self.train = self.data[:len(self.data)//2]
        self.test  = self.data[len(self.data)//2:]
        
        return self
    
    def multivariate_normal(self, num):
        # asself.data.shape = num *  2
        self.data = np.random.multivariate_normal(self.mean,self.cov,size=num)
    
        return self
    
# def lda_accuracy(data, w, b):
#     false_count = 0
#     miss_data    = []
#     for index, item in enumerate(data):
#         lda_val = np.dot(w,item)
#         # class c1
#         if index<100 and lda_val<0:
#             false_count = false_count + 1
#             miss_data   = np.append(miss_data, item)
#         # class c2    
#         elif index>=100 and lda_val>=0:
#             false_count = false_count + 1
#             miss_data   = np.append(miss_data, item)
    
#     accuracy = 1 - false_count/len(data)
#     miss_data = miss_data.reshape(int(len(miss_data)/2),2)
# #     print(miss_data.shape)
    
#     return accuracy, miss_data
    
def accuracy(c1, c2, w, b, var):
    # Calculating accuracy of learned model
    # Using generated data
    acc_c1 = []
    acc_c2 = []
    miss = []
    
    for item in c1:
        bool_c1 = point_loc(item, c1, w, b, var)
        acc_c1.append(bool_c1)
        if not bool_c1:
            miss = np.append(miss, item)
    
    for item in c2:
        bool_c2 = point_loc(item, c2, w, b, var)
        acc_c2.append(bool_c2)
        if bool_c2:
            miss = np.append(miss, item)
        
    acc = (sum(acc_c1)+(100-sum(acc_c2)))/200
    miss = miss.reshape(len(miss)//2, 2)
        
    return acc, miss
    
def gen_line_vec(data_set, w, b, var):
    # This function is for generating decision boundary
    
    # var = W.dot(data_set) + b
    # var = 0 when plotting line for LDA
    # var = 0.5 when plotting line for LR
    
    # Find the min and max value on x axis
    mini = min(data_set[:,0])
    maxi = max(data_set[:,0])
    
    # generating x axis vector (step size 0.1)
    x_vec = np.arange(mini, maxi, 0.1)
    
    # calculating y vector
    y_vec = (-var-b-w[0]*x_vec)/w[1]
    
    return x_vec, y_vec

def point_loc(point, data, w, b, var):
    # var = W.dot(data_set) + b
    # var = 0 when plotting line for LDA
    # var = 0.5 when plotting line for LR
    
    _x, _y = gen_line_vec(data, w, b, var)
    point_a = np.array([_x[0],_y[0]])
    point_b = np.array([_x[-1],_y[-1]])
    
    cross_prod = np.cross(point-point_a, point_b-point_a)
    
    result = (cross_prod < 0) # less than 0 when a point is above the divider
    
    return result
  