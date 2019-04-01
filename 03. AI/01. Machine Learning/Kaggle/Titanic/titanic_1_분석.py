import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
sns.set()

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# print(train.head()) # 알아 보기

# print(train.info()) # 데이터 비어있는 값 분석
# print(train.isnull().sum())
'''
None
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177  나이에 따라 생존여부가 연관되어 있을수도 있으므로 채워넣음
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687  값이 많아 없애는게 나음
Embarked         2  2개 밖에 없으므로 어느값으로 채워도 문제 없엉
dtype: int64
'''

def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['Survived', 'Dead']
    df.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.show()
    plt.savefig('titanic_%s' % feature)
'''
bar_chart('Sex')  # 여자가 남자보다 더 많이 생존
bar_chart('Pclass')  # 1 < 2 < 3 순으로 많이 사망
bar_chart('SibSp')  # 동반 형제자매 / 배우자 0명일수록 많이 사망
bar_chart('Parch')  # 위와 비슷
bar_chart('Embarked')  # S, Q 는 많이 사망. 상대적으로 C는 덜 사망
'''
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


######################### 모델링
'''
이제 가장 높은 정확도를 보이는 모델을 찾은 다음 Test Set의 Survived 즉 생존 여부를 예측하는 과정을 진행
먼저 Train Set을 X와 Y값로 나누어 줍니다. 아래에서 Train_data가 X이고 target이 Y라고 볼 수 있습니다.
'''

train_data = train.drop('Survived', axis=1)
target = train['Survived']

# print(train_data.shape, target.shape)
# print(train.info())  # Null 값이 업따!

k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

clf = RandomForestClassifier(n_estimators=20) # 13개의 decision tree 사용

scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(round(np.mean(score)*100, 2))
