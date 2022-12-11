from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

import matplotlib.pyplot as plt
# MAIN
# Read data
df = pd.read_csv('models/spam.csv', usecols=[0, 1], encoding='latin-1')

# Rename columns
df.rename(columns={'v1': 'Category', 'v2': 'Message'}, inplace=True)
# print(df.head(5))
df['type'] = df.apply(lambda row: 1 if row.Category == 'ham' else 0, axis=1)
print(df.head(100))

X = list(df['Message'])
# print(X)
y = list(df['type'])
# print(y)


knn = KNeighborsClassifier(n_neighbors=1)

# # print(knn)

# #Split data to 90%data_train and 10% data_test
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9)

# #Instantiate CountVectorizer
vect = CountVectorizer()

# #Training vocabulary
vect.fit(X_train)
# print(vect.vocabulary_)

# #Term frequancy
X_train_dtm = vect.fit_transform(X_train)
print(X_train_dtm)
X_test_dtm = vect.transform(X_test)
# Learning KNN by X_train
knn.fit(X_train_dtm, y_train)

# Prediction by X Test
y_pred = knn.predict(X_test_dtm)

# Compare the prediction result with its target
print("Score: ", accuracy_score(y_pred, y_test))

# Message to test
new = ["URGENT! Your Mobile number has been awarded with a å£2000 prize GUARANTEED"]
dtm = vect.transform(new)

typeofMessage = knn.predict(dtm.toarray())

if typeofMessage == 0:
    print("\""+new[0]+"\" This message is spam")
else:
    print("\""+new[0]+"\" This message is not spam")
