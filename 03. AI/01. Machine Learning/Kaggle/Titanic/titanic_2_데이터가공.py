import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# print(train.describe(include='all'))

def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.show()
    plt.savefig('titanic_%s' % feature)

# 데이터 가공하기

# 1. Cabin과 Ticket 두 값은 삭제(값이 비어있고 연관성이 없다는 판단하에)
# 2. Embarked, Name, Sex 값은 숫자로 변경
# 3. Age의 Null 데이터를 채워 넣을 것
# 4. Age의 값의 범위를 줄일 것(큰 범위는 머신러닝 분석시 좋지 않습니다.)
# 5. Fare의 값도 범위를 줄일 것

### Cabin과 Ticket 삭제
train = train.drop(['Cabin'], axis=1)
test = test.drop(['Cabin'], axis=1)
train = train.drop(['Ticket'], axis=1)
test = test.drop(['Ticket'], axis=1)

### Embarked 값 가공
s_harbor = train[train['Embarked'] == 'S'].shape[0]
q_harbor = train[train['Embarked'] == 'Q'].shape[0]
c_harbor = train[train['Embarked'] == 'C'].shape[0]
# print("S : %s, Q : %s, C : %s" % (s_harbor, q_harbor, c_harbor))

'''
S : 644, Q : 77, C : 168  >> 따라서 빈 값은 S로 대체 
'''

train = train.fillna({"Embarked" : "S"})

embarked_mapping = {"S":1, "C":2, "Q":3}
train['Embarked'] = train['Embarked'].map(embarked_mapping)
test['Embarked'] = test['Embarked'].map(embarked_mapping)


### Name 값 가공
combine = [train, test]
for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
pd.crosstab(train['Title'], train['Sex'])

# Mr, Mrs, Miss, Royal, Rare, Master 6개로 줄어보았고 이를 바탕으로 각 생존률의 평균 살펴보기
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

'''
    Title  Survived
0  Master  0.575000
1    Miss  0.702703
2      Mr  0.156673
3     Mrs  0.793651
4    Rare  0.285714
5   Royal  1.000000   로얄은 100퍼 생존!! 이 데이터를 바탕으로 1부터 6까지로 매핑을 하여 숫자로 변경
'''

title_mapping = {"Mr":1, "Miss":2, "Mrs":3, "Master":4, "Royal":5, "Rare":6}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)

train = train.drop(['Name', 'PassengerId'], axis=1)
test = test.drop(['Name'], axis=1)
combine = [train, test]

sex_mapping = {'male':0, 'female':1}
for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)

### Age 값 가공하기
train['Age'] = train['Age'].fillna(-0.5)
test['Age'] = train['Age'].fillna(-0.5)
bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
train['AgeGroup'] = pd.cut(train['Age'], bins, labels = labels)
test['AgeGroup'] = pd.cut(test['Age'], bins, labels = labels)

# bar_chart('AgeGroup') # Unknown 많이 사망.. Title에 따라 연령 추측해서 넣어보겠음

age_title_mapping = {1:'Young Adult', 2:'Student', 3:'Adult', 4:'Baby', 5:'Adult', 6:'Adult'}

for x in range(len(train['AgeGroup'])):
    if train['AgeGroup'][x] == 'Unknown':
        train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]

for x in range(len(test['AgeGroup'])):
    if test['AgeGroup'][x] == 'Unknown':
        test['AgeGroup'][x] = age_title_mapping[train['Title'][x]]


# AgeGroup 을 숫자로 바꾸고, Age 삭제
age_mapping = {'Baby':1, 'Child':2, 'Teenager':3, 'Student':4, 'Young Adult':5, 'Adult':6, 'Senior':7}
train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
test['AgeGroup'] = test['AgeGroup'].map(age_mapping)

train = train.drop(['Age'], axis=1)
test = test.drop(['Age'], axis=1)

### Fare 범위 쭐이기
train['FareBand'] = pd.qcut(train['Fare'], 4, labels =[1, 2, 3, 4])
test['FareBand'] = pd.qcut(test['Fare'], 4, labels =[1, 2, 3, 4])

train = train.drop(['Fare'], axis=1)
test = test.drop(['Fare'], axis=1)

