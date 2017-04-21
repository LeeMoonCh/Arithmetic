#!coding:utf8

#嗯
from numpy import *


groups = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
labels = array(['A','A','B','B'])
# 结果是4
#print groups.shape[0]
#i = tile([0,0],(4,1))-groups
#print i
#print '*'*20
##通过比较发现对数组求平方值，是对数组里的每一项求平方和，比如[1,2]的平方是[1,4]
#m = i**2
#print groups
#print m
#print '*'*20
#print m.sum(axis=1)#axis=1时代表对数组的行求和
#print m.sum(axis=0)#axis=0时代表对数组的列求和
#d = m.sum(axis=1)**0.5
#print d
#argsort方法是对矩阵中正序排序的后的值在原矩阵中的索引值，比如[2,1,0,5]argsort 后是[0,1,2,5] 在原数组中的索引值为[2,1,0,3]
#print d.argsort()
def classify(intX,dataSet,labels,k):
    #获取数据集数组维度
    dataSetSize = dataSet.shape[0]
    #tile 将intX，转换成一个dataSetSize行1列的矩阵，再减去远数组的值，可以得到[[(Ex-Ax),(Ey-Ay)],[(Ex-Bx),(Ey-By)]....]的数组
#    代表着，输入的intX与dataSet的向量点距离点。
    diffMat = tile(intX,(dataSetSize,1))-dataSet
    #对diffMat做平方计算
    sqDuffNat = diffMat**2
    #对sqDuffNat求和再求平方根
    d = (sqDuffNat.sum(axis=1))**0.5
#   以上表示特征值之间的距离，而k-近岭算法就是根据 这个距离来进行比较分类的
#    获得特征值距离正序排序后的索引值
    indexSort = d.argsort()
    #而k-近岭算法的核心是，选取测量点和样本数据特征值距离最近的k条值，然后再在将这k条值进行排序，取最小的的距离。这个距离对应的分类就是测量点的分类
    
    return labels[indexSort[0]]
#    for i in range(k):
        #需要将前k个距离，和分类一一对应。indexSort是d排序过后的索引值，故，indexSort[i]的值在dataSet，和labels中是一一对应的。
        #我们只需将对应的labels放入对应的classCount中即可。其实，不需要排序就可以
        
  
    
    
    
    
    
     