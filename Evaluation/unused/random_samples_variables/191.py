fig, ax = plt.subplots(figsize=(8,4))
dfTitanic.hist(column="Age", ax=ax);
print(dfTitanic["Age"].describe())