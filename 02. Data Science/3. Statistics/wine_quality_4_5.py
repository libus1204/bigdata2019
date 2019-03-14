import pandas as pd
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'

lm = ols(my_formula, data=wine).fit()
# lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
# lm = smf.glm(formula_all, data=wine_standardized, family = sm.families.Gaussian()).fit()

print("< lm.summary() >")
print(lm.summary())

print("="*80+"\n")
print("\nQuantities you can extract from the result : \n%s" % dir(lm))
print("\nCoefficients : \n%s" % lm.params)
print("\nCoefficient Std Errors : \n%s" % lm.bse)
print("\bAdj. R-squared : \n%.2f" % lm.rsquared_adj)
print("\nF-statistic : %.1f P-value : %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs : %d Number of fitted values : %s" % (lm.nobs, len(lm.fittedvalues)))