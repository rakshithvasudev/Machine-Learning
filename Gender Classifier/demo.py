import numpy as np
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


#classify using decision tree classifier 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict(X)
clfAccuracyScore = accuracy_score(Y,prediction, normalize = False)

#classify using multi-layer perceptron classifier
clf2 = MLPClassifier()
clf2 = clf2.fit(X,Y)
prediction2 = clf2.predict(X)
clfAccuracyScore2 = accuracy_score(Y,prediction2, normalize = False)


#classify using K neighbours classifier
clf3 = KNeighborsClassifier()
clf3 = clf3.fit(X,Y)
prediction3 = clf3.predict(X)
clfAccuracyScore3 = accuracy_score(Y,prediction3, normalize = False)

#classify using Gaussian Naive Bayes classifier
clf4 = GaussianNB()
clf4.fit(X,Y)
prediction4 = clf4.predict(X)
clfAccuracyScore4 = accuracy_score(Y,prediction4, normalize = False)


#check for accuracy 







#print the predicted results
print ("Decision tree classifer: ",prediction, "Having Accuracy score" ,clfAccuracyScore)
print ("MLPClassifier: ", prediction2, "Having Accuracy score" ,clfAccuracyScore2)
print ("KNeighborsClassifier: ",prediction3, "Having Accuracy score" ,clfAccuracyScore3)
print ("GaussianNB: ",prediction4,  "Having Accuracy score" ,clfAccuracyScore4)

