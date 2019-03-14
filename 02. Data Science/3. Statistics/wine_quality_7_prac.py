import pandas as pd
from statsmodels.formula.api import ols, glm

print("7.2.7 예측하기")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')



# 2
my_formula2 = 'quality ~ alcohol'
lm = ols(my_formula2, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
correct_per = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 50.50%

# 3
my_formula = 'quality ~ alcohol + chlorides'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 50.43%

# 4
my_formula = 'quality ~ alcohol + chlorides + citric_acid'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 50.48%

# 5
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 50.42%
# print(correct_per)

# 6
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 50.47%

# 7
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 정답률 50.20%

# 8
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)   # 정답률 50.23%

# 9
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100) # 전체 정답률 50.75%

# 10
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100) # 전체 정답률 51.53%

# 11
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates + total_sulfur_dioxide'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
correct_per.append(correct.count(0)/len(correct)*100)  # 전체 정답률 52.19%

# 12
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)

print(correct.count(0)/len(correct)*100) # 전체 정답률 53.33%

# 13
my_formula = 'quality ~ alcohol + citric_acid + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)

print(correct.count(0)/len(correct)*100) # 전체 정답률 53.35%

# 14
my_formula = 'quality ~ alcohol + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)

# print(correct.count(0)/len(correct)*100) # 전체 정답률 53.16%

# 15
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + sulphates + total_sulfur_dioxide'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)

# print(correct.count(0)/len(correct)*100) # 전체 정답률 51%

# 16
my_formula = 'quality ~ chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)

# print(correct.count(0)/len(correct)*100) # 전체 정답률 53.12%

# 17
my_formula = 'quality ~ alcohol + citric_acid + density + fixed_acidity + free_sulfur_dioxide +' \
             'pH + residual_sugar + sulphates + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]
correct = []
for count in range(len(y_predicted_rounded)):
    a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
    correct.append(a)
# print(correct.count(0)/len(correct)*100) # 전체 정답률 53.30%

# def combination(arr, r):
#     arr = sorted(arr)
#     def generate(chosen):
#         if len(chosen) == r:
#             my_formula = 'quality ~ '+ chosen[0]
#             lm = ols(my_formula, data=wine).fit()
#             dependent_variable = wine['quality']
#             independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
#             new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
#             y_predicted = lm.predict(new_observations)
#             y_predicted_rounded = [round(score) for score in y_predicted]
#             correct = []
#             correct_max=[]
#             for count in range(len(y_predicted_rounded)):
#                 a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
#                 correct.append(a)
#             print(correct.count(0) / len(correct) * 100)
            # return
        # start = arr.index(chosen[-1]) + 1 if chosen else 0
        # for nxt in range(start, len(arr)):
        #     chosen.append(arr[nxt])
        #     generate(chosen)
        #     chosen.pop()
    # generate([])
# list = []
# combination(['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity'], 3)
# print(list)
# for count in combination(['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity'], 1):
#     print(count)
#     my_formula = count[0]
#     lm = ols(my_formula, data=wine).fit()
#     dependent_variable = wine['quality']
#     independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
#     new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
#     y_predicted = lm.predict(new_observations)
#     y_predicted_rounded = [round(score) for score in y_predicted]
#     correct = []
#     for count in range(len(y_predicted_rounded)):
#         a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
#         correct.append(a)
#     print(correct.count(0)/len(correct)*100)

def combination(arr, r):
    arr = sorted(arr)
    def generate(chosen):
        if len(chosen) == r:
            my_formula = 'quality ~ '+ chosen[0] +'+'+ chosen[1]+'+' + chosen[2]
            lm = ols(my_formula, data=wine).fit()
            dependent_variable = wine['quality']
            independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
            new_observations = wine.ix[wine.index.isin(range(6497)), independent_variables.columns]
            y_predicted = lm.predict(new_observations)
            y_predicted_rounded = [round(score) for score in y_predicted]
            correct = []
            correct_max=[]
            for count in range(len(y_predicted_rounded)):
                a = int(wine['quality'][count]) - int(y_predicted_rounded[count])
                correct.append(a)
            # print(chosen)
            correct_max.append(correct.count(0) / len(correct) * 100)
            print(max(correct_max))
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination(['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH',
                 'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity'], 3)