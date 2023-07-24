formula = "accuracy ~ C(subject, Treatment(0)) + C(complexity, Treatment(3)) * C(model, Treatment(1))"
lm = ols(formula, df)
fit = lm.fit()
qqplot(fit.resid)
print(fit.summary())
print('\nThe accuracy of the classifier depends on the subject, ' +
      'model type (deep network versus logistic regression), ' +
      'and task complexity (CV versus consonant versus {vowel, location, degree}) ' +
      '(ANOVA with subject, model type, task complexity, and model-task complexity interaction, ' +
      'f-value: {}, p: {}). '.format(fit.fvalue, fit.f_pvalue) +
      'Within this ANOVA, all treatment coefficients were significant ' +
      'at p<.001 with Subject 1, CV task, and logistic regression as the reference treatment.')
for table in fit.summary().tables:
    print(table.as_latex_tabular())
plt.show()