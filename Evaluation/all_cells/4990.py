def calculate_factor(f_neighb_first, neighbour_msg_prod):
    #Numpy by default broadcast the first dimension,
    #therefore it is not necessary to expand the messages tensor manually

    return f_neighb_first * neighbour_msg_prod

#To check the broadcast is indeed right
#P = np.arange(2*3).reshape(2, 3)
#Q = np.arange(5*2*3).reshape(5, 2, 3)
#print(all(Q * P == Q * P[None, ...]))