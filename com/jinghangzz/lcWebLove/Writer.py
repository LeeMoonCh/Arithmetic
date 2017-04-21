#!coding:utf8
from numpy import *
from dircache import listdir
from com.jinghangzz.k_near import classify


#因为数据集是一个32*32的文件
def getImage(fileName):
    #新建一个列表
    ia = []
    #打开一个文件
    fileLines = open(fileName)
    #循环32次，每次读一行
    for i in range(32):
        line = fileLines.readline()
        #循环32次，每次取一个值，将这个值append到list里
        for j in range(32):
            #这个步骤，是将矩阵的第一行的每个元素都赋值，这个值就是每行数据中的值
            ia.append(int(line[j]))
    return ia

#listdir方法，将目标目录下的所有文件和文件夹都给以字符串的形式放入一个列表中
listD = listdir("G:\\2")
#print listD
#学习集的list和分类list
dataSet = []
labels = []
for i in range(len(listD)):
    dataSet.append(getImage("G:\\2\\"+listD[i]))
    labels.append(listD[i][0])
#将学习集和分类都转换为numpy的array数组
dataSet = array(dataSet)
labels = array(labels)
#print list.shape[0]
#print dataSet
#print labels
#然后我们需要将测试文件也给转换成对应的数据
listT = listdir("G:\\1")
count = 0
for m in range(len(listT)):
    testList = getImage("G:\\1\\"+listT[m])
    result = classify(testList,dataSet,labels,20)
    if(int(result) != int(listT[m][0])):
        count +=1

print "错误率为:"+str(float(count)/len(listT))






