import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn import metrics
import warnings
import seaborn as sns

print("Question#1")
sns.set(style="white", color_codes=True)

warnings.filterwarnings("ignore")

df=pd.read_csv("datasets/Salary_Data.csv")
print(df.head())

X = df.iloc[:, :-1].values
Y = df.iloc[:, 1].values
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=1/3, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

Y_Pred = regressor.predict(X_Test)

print(mean_squared_error(Y_Test, Y_Pred))

plt.title('Training data')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.scatter(X_Train, Y_Train)
print(plt.show())


plt.title('Testing data')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.scatter(X_Test, Y_Test)
print(plt.show())

print("\n")
print("Question#2")
df2=pd.read_csv("datasets/K-Mean_Dataset.csv")
print(df2.head())

X = df2.iloc[:, 1:].values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X)
X = imputer.transform(X)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

nclusters = 4 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
print(km.fit(X))

print("----")
y_cluster_kmeans = km.predict(X)
score = metrics.silhouette_score(X, y_cluster_kmeans)
print('Silhouette score:', score)

print("\n")
print("Question#3")
scaler = preprocessing.StandardScaler()
scaler.fit(X)
X_scaled_array = scaler.transform(X)
X_scaled = pd.DataFrame(X_scaled_array)



nclusters = 4
km = KMeans(n_clusters=nclusters)
print(km.fit(X_scaled))
print("")
y_scaled_cluster_kmeans = km.predict(X_scaled)

score = metrics.silhouette_score(X_scaled, y_scaled_cluster_kmeans)
print('Silhouette score after applying scaling:', score)