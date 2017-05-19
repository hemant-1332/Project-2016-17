#import sklearn
from sklearn import tree
#collect data
features = [[130, 0], [140,0], [150, 1], [170, 1]]  #input 0=smooth, 1=rough
labels = [0, 0, 1, 1]  #output, 0=apple, 1=orange

#create classifier = box of rules
clf = tree.DecisionTreeClassifier()

#train classifier
clf = clf.fit(features, labels)  #finding pattern, learning algo

#test ur classifier by giving sample input
print clf.predict([180, 1]) #feature is input