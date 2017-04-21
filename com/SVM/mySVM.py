#coding:utf8
from numpy import *
import pylab
from time import sleep

#我们先拿到数据
dataSet=[]
dataLabels=[]
fileR = open("testSet.txt")
for line in fileR.readlines():
    #看看数据是否读取到了
    #print line
    words = line.strip().split("\t")
    dataSet.append([float(words[0]),float(words[1])])
    dataLabels.append(float(words[2]))
#取得dataSet的行数和列数，组成一个dataSet行数1列的新矩阵，这个矩阵的所有值为0
#dataSet = mat(dataSet)
#print dataSet
#print dataSet[1,:] #这里说一下这个numpy矩阵的[n,:]和[:,n]这分别取得是矩阵的第n行和第n列
#print dataSet[1,:].T #注意这里就是w^T的公式表达式的代码部分
#listN = shape(dataSet)
#print zeros((listN[0],1))
#print mat(dataLabels).transpose()
#print multiply(zeros((listN[0],1)),dataSet) #每行相乘，得到一个新的结果
def simpleSMO(dataSet,labels,t,maxIter,C=0.6):
    #参数说明，dataSet是学习集，labels是学习集对应的标签。C为松弛变量-->允许有些数据点可以处于分隔面的错误一侧。t为容错率；maxIter为最大迭代次数
    dataSet=mat(dataSet);labels=mat(labels).transpose()#将dataSet和lables都转换成矩阵，其中labels转换成和dataSet一样行数的矩阵，方便之后计算
    m,n=shape(dataSet)#取得dataSet的行数和列数
    alphas = mat(zeros((m,1)))#初始化alphas-->这个alphas是我们主要的求解对象，但是怎么推到出来我们需要求解这个alphas的，我还没搞明白
    b=0 #初始化b
    iterI = 0 #初始化迭代次数
    while iterI<maxIter:#这个外部循环，一共循环maxIter次
        alphaPairsChanged = 0 #记录alpha是否已经进行优化，每次循环时设为0，然后再对整个集合顺序遍历
        for i in range(m):
            fXi = float(multiply(alphas,labels).T*(dataSet*dataSet[i,:].T)) +b # 我们预测的类别。我们的alphas矩阵和labels矩阵进行multiply操作
            #得到的是一个100行1列的矩阵再转置就变成了一个1行100列的矩阵，然后我们的学习集的第i行的转置就是一个2行1列的矩阵，而学习集是一个100*2的矩阵，他们相乘会得到一个
            #100行1列的矩阵。一个1行100列的矩阵和一个100行1列的矩阵相乘的结果是一个值，这个值就是我们要求的类别
#            print multiply(alphas,labels).T
#            print dataSet*dataSet[i,:].T
#            print fXi
#            print labels[i]
#            break
            Ei = fXi - float(labels[i])#检查是否违反KKT条件 误差：基于这个实例的预测结果和真实结果的比对，计算误差Ei 参考：http://blog.csdn.net/puqutogether/article/details/44587653
            #我对这个公式的理解就是，fXi是我们根据学习集和相应的标签算出来的类别信息。Ei的值越大就代表越偏离真。
            if ((labels[i]*Ei < -t) and (alphas[i] < C)) or ((labels[i]*Ei > t) and (alphas[i] > 0)): #不管是正负间隔都会测试，同时检查alpha值，保证其不能等于0或C
            #我的理解是，Ei是测试分类和真实类别的误差，t是我们的容错率，labels[i]不是1就是-1，而Ei在第一次循环进入后绝对是labels[i]的反面，也就是说labels[i]*Ei决对是负数。
#                pass
                









        break
simpleSMO(dataSet,dataLabels,0.001,40)































