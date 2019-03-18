import pandas as pd
from statsmodels.formula.api import ols,glm

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
            'pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data = wine).fit()
print(lm.summary())