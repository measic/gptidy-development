firstClassMRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 1) & (dfTitanic["Sex"] == "male"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 1) & (dfTitanic["Sex"] == "male"), ["Survived"]].count())
firstClassFRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 1) & (dfTitanic["Sex"] == "female"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 1) & (dfTitanic["Sex"] == "female"), ["Survived"]].count())
secondClassMRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 2) & (dfTitanic["Sex"] == "male"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 2) & (dfTitanic["Sex"] == "male"), ["Survived"]].count())
secondClassFRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 2) & (dfTitanic["Sex"] == "female"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 2) & (dfTitanic["Sex"] == "female"), ["Survived"]].count())
thirdClassMRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 3) & (dfTitanic["Sex"] == "male"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 3) & (dfTitanic["Sex"] == "male"), ["Survived"]].count())
thirdClassFRate = (dfTitanic.loc[(dfTitanic["Survived"] == 1) & (dfTitanic["Pclass"] == 3) & (dfTitanic["Sex"] == "female"), ["Survived"]].count() / dfTitanic.loc[(dfTitanic["Pclass"] == 3) & (dfTitanic["Sex"] == "female"), ["Survived"]].count())
print("First Class Male Fraction: {0:.4f} \t First Class Female Fraction {1:.4f}\nSecond Class Male Fraction: {2:.4f} \t Second Class Female Fraction {3:.4f}\nThird Class Male Fraction: {4:.4f} \t Third Class Female Fraction {5:.4f}".format(firstClassMRate["Survived"], firstClassFRate["Survived"], secondClassMRate["Survived"], secondClassFRate["Survived"], thirdClassMRate["Survived"], thirdClassFRate["Survived"]))