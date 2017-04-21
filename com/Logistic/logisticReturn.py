#coding:utf8

from numpy import *



fr = open("G:\\testSet.txt")
dataSet = []
labels = []
#将每行的数据切分开了，放入一个学习集，和相对应的类别中，Logistic回归属于监督学习，所以必须有学习集。
for line in fr.readlines():
    words = line.strip().split()
    dataSet.append([1.0,float(words[0]),float(words[1])])
    labels.append([float(words[2])])

#print dataSet
#print labels        
#开始设计训练算法,参数为学习集合和对应的类别标签数据集
def LogisticRe(dataSet,labels,inX):
    #将dataSet和labels都转换成矩阵。
    dataSet = mat(dataSet)
    labels = mat(labels)
    #numpy的shape函数，可以取到矩阵的行数和列数，如m,n=shape(dataSet)--->m是dataSet的行数，n是列数
    m,n=shape(dataSet)
    #numpy的ones函数，参数为一个(m,n)，可以将n转换成一个m*1的矩阵，而矩阵的值都是n
    #初始化系数矩阵，系数矩阵根据梯度上升法得到一个最好的系数矩阵。
    modulus = ones((n,1))
    alpha = 0.001
    for i in range(inX):
        #这里需要注意一个点，矩阵相乘必须符合A*B，A=m*n,B=n*j-->也就是A的列数等于B的行数，
        #h是dataSetsigmoid值的矩阵
        h = 1.0/(1+exp(-(dataSet*modulus))) #这里特别注意，dataSet和modulus的位置不能互换。因为modulus生产的矩阵为m*1，而m是dataSet的列数
        error = (labels-h) #这里为什么可以相减？矩阵乘法，得到的新矩阵的行数是A的行数，列数是B的列数。这里h就是dataSet的行数*1，而labels也是一样的结构。
        modulus = modulus + alpha*dataSet.transpose()*error #transpose是numpy的一个转换函数，将m*n的矩阵转换成n*m的矩阵
    return modulus #最后返回，梯度上升后得到的modulus矩阵，这个矩阵就是最优系数

print LogisticRe(dataSet, labels, 500)

def randomLogistic(dataSet,labels,numIter=150):
    m,n = shape(dataSet) #得到学习集的行列数。
    modulus = ones(n) #生产一个1行n值得数组
    for j in range(numIter): #开始迭代，默认150次、
        index =  range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.001 #虽然看懂它这样写。是为了每次循环alpha值都根据j和i改动，但这个公式我并不知道为什么这样写
            randIndex = int(random.uniform(0,len(index))) #随机的从0~len(index)中取得一个值，作为随机数
            h = 1.0/(1.0+exp(sum(-(dataSet[randIndex]*modulus)))) #这里的exp的参数是，dataSet的随机数行和系数相乘之后的数组项之和。
            error = labels[randIndex]-h
            modulus = modulus + alpha*error*dataSet[randIndex]
            del(index[randIndex]) #将随机过的下标删除掉
    return modulus

print randomLogistic(dataSet, labels,500)


def classifyLogistic(dataSet,modulus):
    p = 1.0/(1.0+exp(-sum(dataSet*modulus)))
    if p>0.5 :
        return 1
    else :
        return 0










