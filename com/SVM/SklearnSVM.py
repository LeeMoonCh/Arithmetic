#coding:utf8

from sklearn import svm

dataSet=[]
dataLabels=[]
fileR = open("testSet.txt")
for line in fileR.readlines():
    #看看数据是否读取到了
    #print line
    words = line.strip().split("\t")
    dataSet.append([float(words[0]),float(words[1])])
    dataLabels.append(float(words[2]))

clf = svm.SVC()#新建一个SVC的实例，嗯SVC是支持响亮分类，C就是classify。还有一个SVR是支持响亮回归，R就是return
clf = clf.fit(dataSet,dataLabels) #放入训练集和训练f
print clf.predict([1,2])
















