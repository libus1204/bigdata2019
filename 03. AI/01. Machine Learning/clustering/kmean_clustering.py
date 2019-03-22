import pandas as pd
import numpy as np
import sklearn.cluster, sklearn.preprocessing
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.DataFrame(columns=["x", "y"])

df.loc[0] = [3, 1]
df.loc[1] = [4, 1]
df.loc[2] = [3, 2]
df.loc[3] = [4, 2]
df.loc[4] = [10, 5]
df.loc[5] = [10, 6]
df.loc[6] = [11, 5]
df.loc[7] = [11, 6]
df.loc[8] = [15, 1]
df.loc[9] = [15, 2]
df.loc[10] = [16, 1]
df.loc[11] = [16, 2]

print(df.head(20)) # 데이터프레임 차트형식

sns.lmplot('x', 'y', data=df, fit_reg=False, scatter_kws={"s": 200}) # x-axis, y-axis, no line, marker size

plt.title('kmean plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

data_points = df.values # convert dataframe to numpy array
kmeans = sklearn.cluster.KMeans(n_clusters=3).fit(data_points)

kmeans.labels_ # cluster id for each data point

kmeans.cluster_centers_ # this is final centroids position

df['cluster_id'] = kmeans.labels_
df.head(12)

# x,y-axis, data, no line, marker size, color
sns.lmplot('x', 'y', data=df, fit_reg=False, scatter_kws={"s": 150}, hue="cluster_id")
plt.title('after kmean clustering')
plt.show()