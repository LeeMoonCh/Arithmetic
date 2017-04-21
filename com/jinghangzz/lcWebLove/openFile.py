#coding:utf8
#打开相应文件
import matplotlib 
import matplotlib.pyplot as plt
from numpy import *
from com.jinghangzz.k_near import classify
from com.jinghangzz.autoOne import autoOne, testAutoOne
file = open("G:\\datingTestSet2.txt")
#file 读取内容，一行一行的读。
lines=file.readlines()
#新建两个数组分别对应学习样本数据集，和类别
a=[]
b=[]
c=[]
linesArray = []
labels = []
#遍历lines
for line in lines:
    line = line.strip()
    list = line.split('\t')
    #将三个感兴趣特征加入相对应的数组中
    a.append(float(list[0]))
    b.append(float(list[1]))
    c.append(float(list[2]))
    labels.append([float(list[3])])
#对a,b,c数组进行归一化
mins,n = autoOne(a,b,c)
#遍历。然后将a,b,c的值赋给linesArray
for i in range(len(a)):
    linesArray.append([a[i],b[i],c[i]])
    
#将linesArray和labels都转化为numpy数组。
linesArray = array(linesArray)
labels = array(labels)
#对于
#print linesArray
#print linesArray[999,0]
#使用matplotlib画出图形
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(linesArray[:,0],linesArray[:,1],15.0*labels,15.0*labels)
#plt.show()
#print linesArray
#print labels
#导入classify函数，对新的数据点进行分类
list = testAutoOne(mins,n,[40920,8.1,1])
x = classify(list,linesArray,labels,20)
print x







