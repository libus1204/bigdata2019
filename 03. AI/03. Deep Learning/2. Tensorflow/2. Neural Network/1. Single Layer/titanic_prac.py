import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2.5)

import missingno as msno

import warnings
warnings.filterwarnings('ignore')

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# print(df_train.head())

# print(df_train.describe())

# for col in df_train.columns:
#     msg = 'column : {:>10}\t Percent of NaN value : {:.2f}%'.format(col, 100 * (df_train[col].isnull().sum() / \
#                                                                                df_train[col].shape[0]))
#     print(msg)
# for col in df_test.columns:
#     msg = 'column : {:>10}\t Percent of NaN value : {:.2f}%'.format(col, 100 * (df_test[col].isnull().sum() / \
#                                                                                df_test[col].shape[0]))
#     print(msg)
# msno.matrix(df = df_train.iloc[:, :], figsize=(8, 8), color = (0.8, 0.5, 0.2))
# msno.bar(df=df_test.iloc[:, :], figsize=(8, 8), color=(0.8, 0.5, 0.2))

# f, ax = plt.subplots(1, 2, figsize=(18, 8))
# df_train['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
# ax[0].set_title('Pie plot - Survived')
# ax[0].set_ylabel('')
# sns.countplot('Survived', data = df_train, ax=ax[1])
# ax[1].set_title('Count plot - Survived')
# plt.show()

# print(df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).count()) # 각 클래스의 사람 수
# print(df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).sum()) # 그 클래스에서 생존자 수

print(pd.crosstab(df_train['Pclass'], df_train['Survived'], margins=True))
    # .style.background_gradient(cmap='summer_r')

df_train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=True).mean().sort_values(by='Survived', \
                                                                                       ascending=False).plot.bar()


