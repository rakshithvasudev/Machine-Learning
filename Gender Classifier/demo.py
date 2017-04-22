from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB



# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']



clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[170,70,37]])

clf2 = MLPClassifier()
clf2 = clf2.fit(X,Y)
prediction2 = clf2.predict([[170,70,37]])

clf3 = KNeighborsClassifier()
clf3 = clf3.fit(X,Y)
prediction3 = clf3.predict([[170,70,37]])

clf4 = GaussianNB()
clf4.fit(X,Y)
prediction4 = clf4.predict([[170,70,37]])

print ("Decision tree classifer: ",prediction)
print ("MLPClassifier: ", prediction2)
print ("KNeighborsClassifier: ",prediction3)
print ("GaussianNB: ",prediction4)