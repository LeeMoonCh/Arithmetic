# coding:utf8

from numpy import *
import matplotlib.pylab as plt
fr = open("ex0.txt")
xArr = []
yArr = []
for line in fr.readlines():
    words = line.strip().split("\t")
    #为了代码的复用率，我们应该写一个for循环
    xArrEch = []
    for i in range(len(words)-1):
        xArrEch.append(float(words[i])) #每一行的特征组成一个数据组。
    xArr.append(xArrEch) #将每行的特征数据组加入到xArr中
    yArr.append(float(words[-1])) #每一行的最后一个值是真实值
#print xArr
#print yArr
def getReturn(xArr,yArr):
    #参数说明：xArr是特征值，yArr是真实的结果集
    #将数组都转成矩阵
    xArr = mat(xArr)
    yArr = mat(yArr).T
    #X^T*X的代码实现
    xTx = xArr.T*xArr
    if linalg.det(xTx) == 0 : #因为要用到xTx的逆矩阵，所以事先需要确定计算得到的xTx是否可逆，条件是矩阵的行列式不为0
        #linalg.det(xTx)求二阶矩阵，如果为0那么代表矩阵列为0
        print "矩阵不可逆"
        return
    #使用公式得到最佳回归系数，w^=(X^T*X)^-1*(X^T*y)
    return xTx.I*(xArr.T*yArr)
#观看你和曲线
#wr = getReturn(xArr, yArr)
#xMat = mat(xArr)
#yMat = mat(yArr)
#fig = plt.figure()
#ax = fig.add_subplot(111)               #add_subplot(349)函数的参数的意思是，将画布分成3行4列图像画在从左到右从上到下第9块
##画出散点图
#ax.scatter(xMat[:, 1].flatten(), yMat.T[:, 0].flatten().A[0]) #scatter 的x是xMat中的第二列，y是yMat的第一列
##画出直线图，直线公式y=ax+b
#xCopy = xMat.copy() 
#xCopy.sort(0)
#yHat = xCopy * wr
#ax.plot(xCopy[:, 1], yHat)
#plt.show()
#
#print corrcoef(yMat,yHat.T)

#局部加权线性回归
def lwlr(testData,xArr,yArr,k=0.1):
    #参数说明，testData测试数据。xArr学习样本点，yArr真实值。k高斯核k值
    xArr = mat(xArr); yArr = mat(yArr).T #矩阵的T方法是转置，I方法是求逆矩阵也就是对应W^-1
    m = shape(xArr)[0]                    #获得xMat矩阵的行数
    weights = mat(eye((m)))               #eye()返回一个对角线元素为1，其他元素为0的二维数组，创建权重矩阵
    '''
    [[ 1.  0.  0.  0.]
     [ 0.  1.  0.  0.]
     [ 0.  0.  1.  0.]
     [ 0.  0.  0.  1.]]'''#这就是eye做出来的一个对角矩阵。有值得地方 分别对应着w(i,i)
    for j in range(m):
        diffMat = testData - xArr[j,:]     #遍历数据集，计算每个样本点对应的权重值;一般测试数据是一行数据，这个相减的结果就是公式中的x^i-x.
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))   #k控制衰减的速度。公式|x^i-x|就是diffmat*diffmat.T的乘积
        #遍历完之后，我们的weights的对角值就都改变了
    #套用公式
    xTx = xArr.T*(weights*xArr)
    if linalg.det(xTx) == 0:
        print "矩阵不可逆"
        return
    wr = xTx.I*(xArr.T*(weights*yArr))
#    print testData*wr
    return testData*wr #这个结果是一个值，这个值是我们预测的y值

def lwlrTest(testArr,xArr,yArr,k=1.0):
    #参数说明testArr，我们的学习集。xArr--》x坐标，y是实际值。k是高斯核参数。这个方法主要用来测试k，看看k在哪个区间拟合程度最好
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def lwlrTestPlot(xArr,yArr,k=1.0):  #首先将 X 排序，其余的都与lwlrTest相同，这样更容易绘图
    yHat = zeros(shape(yArr))       
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
    return yHat,xCopy

def regression2(xArr,yArr): #主要是看图的方法
    yHat = lwlrTest(xArr, xArr, yArr, 0.01)
    xMat = mat(xArr)
    srtInd = xMat[:,1].argsort(0)           #argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出
    xSort=xMat[srtInd][:,0,:]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:,1], yHat[srtInd])
    ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0] , s=2, c='red')
    plt.show()

#lwlr([1,2], xArr, yArr)
regression2(xArr,yArr)














