print("-> unscaled\n", x_train.iloc[:3,:5])

x_train[x_train.columns[first_numeric_feature:]] = pandas.DataFrame(preprocessing.scale(x_train[x_train.columns[3:]]), 
                                                columns=x_train.columns[3:], 
                                                index=x_train.index)


print("-> scaled\n", x_train.iloc[:3,:5])