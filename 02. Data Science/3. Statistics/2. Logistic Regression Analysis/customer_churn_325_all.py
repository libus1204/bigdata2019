# 목적 : 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm
from itertools import combinations
import operator
# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                            churn['night_charge'] + churn['intl_charge']

# Fit a logistic regression model
dependent_variable = churn['churn01']
# independent_variables = churn[['account_length', 'vmail_plan', 'vmail_message', 'day_mins', 'day_calls',
#                                'day_charge', 'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls',
#                                'night_charge', 'intl_mins', 'intl_calls', 'intl_charge', 'cust_serv_calls']]
independent_variables_list = ['account_length', 'vmail_message', 'day_mins', 'day_calls',
                              'day_charge', 'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls',
                              'night_charge', 'intl_mins', 'intl_calls', 'intl_charge', 'custserv_calls']
correct_per_max = 0
count2 = 0
for num in range(1,16):
    combi_list = list(combinations(independent_variables_list, num))
    for tup in combi_list:
        # print(count2)
        count2 += 1
        independent_variables = churn[list(tup)]
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
        new_observatios = churn.ix[churn.index.isin(range(3333)), independent_variables.columns]
        new_observatios_with_constant = sm.add_constant(new_observatios, prepend=True)
        y_predicted = logit_model.predict(new_observatios_with_constant)
        y_predicted_rounded = [round(score, 0) for score in y_predicted]
        logistic_predicted_value_list = []
        for predict_value in y_predicted_rounded:
            if predict_value == 0.0:
                logistic_predicted_value_list.append(False)
            else:
                logistic_predicted_value_list.append(True)
        print(count2)
        correct = 0
        for count in range(3333):
            if str(logistic_predicted_value_list[count]) == str(churn['churn'][count][0:-1]):
                correct += 1
                a = (correct / 3333) * 100
                if correct_per_max < a:
                    correct_per_max = a
                # print(correct_per_max)

print(correct_per_max)