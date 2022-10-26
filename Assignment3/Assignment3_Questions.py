import pandas as pd
from sklearn.svm import SVC, LinearSVC


train_df = pd.read_csv('C:/Users/Administrator/Documents/GitHub/ML/Assignment3/Dataset/train.csv')
test_df = pd.read_csv('C:/Users/Administrator/Documents/GitHub/ML/Assignment3/Dataset/train.csv')

print(train_df.isnull().sum())
print("\n")

print('-'*10)
print("\n")

print(test_df.isnull().sum())
print("\n")

print("\n")
X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]

X_test = test_df.drop("PassengerId",axis=1)

print("\n")

svc = SVC(max_iter=1000)

svc.fit(X_train, Y_train)

Y_pred = svc.predict(X_test)

acc_svc = round(svc.score(X_train, Y_train) * 100, 2)

print("svm accuracy =", acc_svc)


# Adding the max_iter parameter and see the resutls
svc = LinearSVC()

svc.fit(X_train, Y_train)

Y_pred = svc.predict(X_test)

acc_svc = round(svc.score(X_train, Y_train) * 100, 2)

print("svm accuracy =", acc_svc)