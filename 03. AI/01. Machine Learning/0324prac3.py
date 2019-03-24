# import pandas as pd
# import sklearn.cluster, sklearn.preprocessing
# from sklearn import metrics
#
# alcohol2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")
# columns = ["Wine", "Beer"]
#
# k_means = sklearn.cluster.KMeans(n_clusters=9)
#
# k_means.fit(alcohol2009[columns])
# alcohol2009["Clusters"] = k_means.labels_
#
# alcohol2009.to_csv("Clustering_Result.csv", index = False)
#
# data = alcohol2009[["Wine", "Beer"]]
# label = alcohol2009["Clusters"]
#
# predicted_result = k_means.predict(data)
# print("예측 클러스터링 결과")
# print(predicted_result)
#
# print("정답률 : %s %%" % (metrics.accuracy_score(label, predicted_result)*100))
# import pandas as pd
# import sklearn.preprocessing, sklearn.cluster
# from sklearn import metrics
#
# alcohol = pd.read_csv("niaaa-report2009.csv", index_col="State")
# columns = ["Wine", "Beer"]
# k_means = sklearn.cluster.KMeans(n_clusters=9)
# k_means.fit(alcohol[columns])
# alcohol["Cluster"] = k_means.labels_
# alcohol.to_csv("Clustering_Result.csv", index=False)
# data = alcohol[["Wine", "Beer"]]
# label = alcohol["Cluster"]
# predict_result = k_means.predict(data)
# print(predict_result)
# print("정답률 : %s %%" % (metrics.accuracy_score(label, predict_result)*100))
# import pandas as pd
# import sklearn.preprocessing, sklearn.cluster
# from sklearn import metrics
# alcohol = pd.read_csv("niaaa-report2009.csv", index_col = "State")
# columns = ["Wine", "Beer"]
# kmeans = sklearn.cluster.KMeans(n_clusters=9)
# kmeans.fit(alcohol[columns])
# alcohol["Cluster"] = kmeans.labels_
# alcohol.to_csv("Clustering_result.csv", index=False)
# data = alcohol[columns]
# label = alcohol["Cluster"]
# predicted_result = kmeans.predict(data)
# print(predicted_result)
# print("정답률 : %s %%" % (metrics.accuracy_score(label, predicted_result)*100))
# import pandas as pd
# import sklearn.preprocessing, sklearn.cluster
# from sklearn import metrics
# alcohol = pd.read_csv("niaaa-report2009.csv", index_col="State")
# columns = ["Wine", "Beer"]
# kmeans = sklearn.cluster.KMeans(n_clusters=9)
# kmeans.fit(alcohol[columns])
# alcohol["Clusters"] = kmeans.labels_
# alcohol.to_csv("Clustering_result.csv", index=False)
# data = alcohol[columns]
# label = alcohol["Clusters"]
# predicted_result = kmeans.predict(data)
# print(predicted_result)
# print("정답률 : %s %%" % (metrics.accuracy_score(label, predicted_result)*100))
# import pandas as pd
# from sklearn import metrics
# import sklearn.cluster, sklearn.preprocessing
# alcohol = pd.read_csv("niaaa-report2009.csv", index_col = "State")
# columns = ["Wine", "Beer"]
# kmeans = sklearn.cluster.KMeans(n_clusters=9)
# kmeans.fit(alcohol[columns])
# alcohol["Clusters"] = kmeans.labels_
# alcohol.to_csv("Clustering_result.csv", index=False)
# data = alcohol[columns]
# label = alcohol["Clusters"]
# predict = kmeans.predict(data)
# print(predict)
# print("정답률 : %s %%" % (metrics.accuracy_score(label, predict)*100))
import pandas as pd
from sklearn import metrics
import sklearn.preprocessing, sklearn.cluster
alcohol = pd.read_csv("niaaa-report2009.csv", index_col="State")
columns = ["Wine", "Beer"]
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alcohol[columns])
alcohol["Clusters"] = kmeans.labels_
alcohol.to_csv("Clustering_result.csv", index=False)
data=alcohol[columns]
label=alcohol["Clusters"]
predict = kmeans.predict(data)
print(predict)
print("정답률 : %s %%" % (metrics.accuracy_score(label, predict)*100))