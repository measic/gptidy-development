# Most important variables in Information Gain
if __name__ == '__main__':
    for Variable in Q_Cat:
        A = Information_Gain[Variable]
        A = A.sort_values('Information Gain', ascending=False)
        A.name = Variable
        print(Variable)
        print(A.head())