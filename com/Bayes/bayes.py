#coding:utf8

from numpy import *
from com.getMydict import saveData

def trainProb(dataSet,classCategory,filename):
    #训练算法,参数含义：dataSet代表已经数字化(脏字用1表示，非脏字用0表示)过后的文档集；classCategory代表和dataSet对应的类别，分别用0--非侮辱，1--侮辱表示
    #那么现在想想，我们想要训练算法，就是根据文档中脏字出现的概率和它对应的类别形成一个新的数据集，这个数据集分别是[[脏字概率,类别]]
    #然后根据k-近岭算法，得到对应的类别。
    lenDoc = len(dataSet)
    #得到文档总数
    p = 0.0
    listR = []
    for i in range(lenDoc):
        #获得文档中1出现的总次数
        sumP1 = sum(lenDoc[i])
        #取得脏字在
        p = float(sumP1)/len(dataSet[i])
        listR.append([p,classCategory[i]])
    #将数据保存在本地
    saveData(listR,filename)

#之后的思路就是，从本地文件获取listR，dataSet,labels = listR[0],list[1]

def getProb(dataSet):
    #获取一个文档的脏字出现概率
    numP1 = sum(dataSet)
    return float(numP1)/len(dataSet)
        














