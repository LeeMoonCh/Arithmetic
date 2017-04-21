# coding:utf8
from numpy import *

#什么都不说，第一步肯定是得到数据，没有数据搞个毛线的机器学习！
fr = open("testSet.txt")
dataSet = []
for line in fr.readlines():
    words = line.strip().split("\t")
    dataSet.append(map(float,words)) #map函数，words中的所有值都转化为float类型。

#print dataSet
#书上说，我们分簇是按照距离来进行分的，所以写一个求距离的公式，这里使用欧式距离，也就是方差的平方根
def getDistance(x,y):
    return sqrt(sum(power(x-y,2))) #解释下这行代码，sqrt是求平方根。sum是求和，x-y是两个矩阵相见，power中的2 是求x-y的平方

#得到了距离，还有一个随机产生的质心点。随机质心必须要在整个数据集的边界之内，这可以通过找到数据集每一维的最小和最大值来完成。然后生成 0~1.0 之间的随机数并通过取值范围和最小值，以便确保随机点在数据的边界之内。
def getCenter(dataSet,k):
    n = shape(dataSet)[1] #特征数，也就是列数
    centers = mat(zeros((k,n))) #初始化k个质心。
    for j in range(n):  # 创建随机簇质心，并且在每一维的边界内
        minJ = min(dataSet[:,j])  #得到dataSet每列的最小值
        rangJ = float(max(dataSet[:,j])-minJ) #随机范围 最大值-最小值
        centers[:,j] = mat(minJ + rangJ * random.rand(k,1)) #随机生成，并且在每个维度的边界之内
    return centers

#开始写聚类算法
def kMeansCluster(dataSet,k,d=getDistance,c=getCenter):
    #参数说明，dataSet学习集，k就是簇数，d是距离，c就是初始化的质心
    m,n = shape(dataSet)  #获取到dataSet的行和列，因为我们需要对每行进行距离计算
    clusterAssment = mat(zeros((m, 2))) #初始化簇元信息。它对应每行数据的
    centers = c(dataSet,k) #获取初始化的质心
    flag = True #设定开关，这个开关是检查质心是否改变
    while flag == True:
        flag = False
        for i in range(m):  #遍历每条数据
            dist = inf  #初始化距离为无穷大
            index = -1  #初始化行在哪个簇中
            for j in range(k):  #开始比较每行数据到每个质心的距离
                distJI = d(dataSet[i,:],centers[j,:])
                #判断这个距离和最小距离的大小
                if distJI < dist:
                    dist = distJI
                    index = j #改变最小距离和索引。循环完k后的index就是第i行所在的簇
            if clusterAssment[i,0] != index: #判断当前数据所在簇是否和计算得到的索引相当，如果不一样
                flag = True #将开关开了
                clusterAssment[i, :] = index,dist**2
        #行数循环完之后，更新质心。质心是每个簇中所有点的均值
        for center in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A==center)[0]]  #这个nonzero是取得数组中和center一样的数据下标。
            centers[center,:] = mean(ptsInClust, axis=0) #将对应的质心给更改成簇中数据点的均值
    return centers,clusterAssment #返回簇质心，和每行所在簇的元信息
dataSet = mat(dataSet)
print dataSet
print "-----"
myCentroids, clusterAssment = kMeansCluster(dataSet, 4)
print myCentroids
print "-----"
print clusterAssment










