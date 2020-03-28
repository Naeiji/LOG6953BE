import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer


Data = pd.read_csv('reviews_preprocessed.csv', header = None)
# print(Data.head())

# defining the 'y', whether the review belongs to the category or not
category = []
for i in range(len(Data)):
    cat = Data.iloc[i][13]

    if 'hardware' \
       '' in cat:
        category.append(1)
    else: category.append(0)

Data[16] = category
print(category)
# TF-IDF , for n-gram = 1,2,3
tf_idf = TfidfVectorizer(ngram_range=(1, 3))
X = tf_idf.fit_transform(Data[15])
# print(type(X))
# print(X.shape)
Data[17] = X

x_data = X
# print(x_data)
y_data = Data[16]
# print(y_data)
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, stratify= y_data)

clf_GBRT = GradientBoostingClassifier(n_estimators=200)
clf_GBRT.fit(X_train, y_train)
predictions = clf_GBRT.predict(X_test)
acc = clf_GBRT.score(X_test, y_test)
print(acc)
# print(predictions)
# print(y_test)
print(metrics.recall_score(y_test, predictions))
print(metrics.accuracy_score(y_test, predictions))
print(metrics.precision_score(y_test, predictions))
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != predictions).sum()))


