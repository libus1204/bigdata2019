import numpy as np
import pandas as pd
# 목적 : 그룹 별 기술통계 구하기
# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "")\
                 .str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length',
                                'custserv_calls']].agg(['count', 'mean', 'std']))