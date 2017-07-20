import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, accuracy_score
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score


dataset = pd.read_csv("Datasets/Churn_Modelling.csv")
dataset.head()

dataset.info()

X = dataset.iloc[:, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]].values

y = dataset.iloc[:, 13].values

label_enc_X_country = LabelEncoder()
X[:, 1] = label_enc_X_country.fit_transform(X[:, 1])

label_enc_X_gender = LabelEncoder()
X[:, 2] = label_enc_X_gender.fit_transform(X[:, 2])

one_hot_enc = OneHotEncoder(categorical_features=[1])
X = one_hot_enc.fit_transform(X).toarray()

X = X[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# classifier1 = Sequential()
#
# classifier1.add(Dense(units=6, activation='relu', input_dim=11, bias_initializer='uniform'))
#
# classifier1.add(Dense(units=6, activation='relu', bias_initializer='uniform'))
#
# classifier1.add(Dense(units=1, activation='sigmoid', input_dim=11, bias_initializer='uniform'))
#
# classifier1.compile(optimizer='adam', loss='binary_crossentropy',
#                     metrics=['accuracy'])
#
# classifier1.fit(X_train, y_train, epochs=100, batch_size=10)
#
# preds = classifier1.predict(X_test)
#
# preds = (preds > 0.5)
#
#
# cm = confusion_matrix(y_test, preds)
#
# accuracy_score(y_test, preds)
#
# print(classifier1.predict(scaler.transform(np.array([[0.0, 0.0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]]))) > 0.5)
#



def buildclassifier():
    classifier1 = Sequential()
    classifier1.add(Dense(units=6, activation='relu', input_dim=11, bias_initializer='uniform'))
    classifier1.add(Dense(units=6, activation='relu', bias_initializer='uniform'))
    classifier1.add(Dense(units=1, activation='sigmoid', input_dim=11, bias_initializer='uniform'))
    classifier1.compile(optimizer='adam', loss='binary_crossentropy',
                        metrics=['accuracy'])
    return classifier1


classifier1 = KerasClassifier(build_fn=buildclassifier, epochs=100, batch_size=10)
accuracies = cross_val_score(estimator=classifier1, X=X_train, y=y_train, cv=10)

print(accuracies)