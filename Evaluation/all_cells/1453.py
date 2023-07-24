A = np.array(range(1,11))
B = np.array(range(1,6))
C = np.empty(0)
print(A)
print(B)
#remember the base 0 indexing.
for i in range(0,len(A)):
    try:
        C = np.append(C,A[i] + B[i])
        print(C)
    except:
        print('B is too small')
        #sys.exit(1)  #We would use exit(1) to end the script with an error
        break  #use break to just exit the loop without quitting or returning an error code