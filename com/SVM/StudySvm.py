"""
Created on Nov 4, 2010
Update on 2017-03-21
Chapter 5 source file for Machine Learing in Action
@author: Peter/geekidentity
"""
from numpy import *
import pylab
from time import sleep

def main():
    dataArr, labelArr = loadDataSet('testSet.txt')
    smoSimple(dataArr, labelArr, 0.6, 0.001, 40)

def loadDataSet(fileName):
   """
   ���ļ��������н������Ӷ��õ����е����ǩ���������ݾ���
   Args:
       fileName: testSet.txt
   Returns:
       ���ݾ���, ���ǩ
   """
   dataMat = []; labelMat = []
   fr = open(fileName)
   for line in fr.readlines():
       lineArr = line.strip().split('\t')
       dataMat.append([float(lineArr[0]), float(lineArr[1])])
       labelMat.append(float(lineArr[2]))
   return dataMat,labelMat

def selectJrand(i,m):
   """
   ���ѡ��һ������
   Args:
       i: ��һ��alpha���±�
       m: ����alpha����Ŀ
   Returns:
   """
   j=i #we want to select any J not equal to i
   while (j==i):
       j = int(random.uniform(0,m))
   return j

def clipAlpha(aj,H,L):
   """
   ���ڵ�������H��С��L��alphaֵ
   Args:
       aj:
       H:
       L:
   Returns:
   """
   if aj > H:
       aj = H
   if L > aj:
       aj = L
   return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
   """
   SVM SMO�㷨�ļ�ʵ��:
       ����һ��alpha�����������ʼ��Ϊ0����
       ������������С������������ʱ(��ѭ��)
           �����ݼ��е�ÿ����������(��ѭ��):
              ����������������Ա��Ż�:
                  ���ѡ������һ����������
                  ͬʱ�Ż�����������
                  ����������������ܱ��Ż����˳���ѭ��
           �������������û�б��Ż������ӵ�����Ŀ��������һ��ѭ��
   Args:
       dataMatIn: ���ݼ�
       classLabels: ����ǩ
       C: �ɳڱ�����������Щ���ݵ���Դ��ڷָ���Ĵ���һ�ࡣ
           ������󻯼���ͱ�֤�󲿷ֵĺ������С��1.0������Ŀ���Ȩ�ء�
           ����ͨ�����ڸò����ﵽ��ͬ�Ľ����
       toler: �ݴ���
       maxIter: �˳�ǰ����ѭ������
   Returns:
   """
   dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
   b = 0; m,n = shape(dataMatrix)
   alphas = mat(zeros((m,1)))
   iter = 0 # û���κ�alpha�ı������±������ݵĴ���
   while (iter < maxIter):
#       w = calcWs(alphas, dataMatIn, classLabels)
#       print("w:", w)
       alphaPairsChanged = 0 #��¼alpha�Ƿ��Ѿ������Ż���ÿ��ѭ��ʱ��Ϊ0��Ȼ���ٶ���������˳�����
       for i in range(m):
           fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b # ����Ԥ������
           Ei = fXi - float(labelMat[i])#����Ƿ�Υ��KKT���� ���������ʵ����Ԥ��������ʵ����ıȶԣ��������Ei �ο���http://blog.csdn.net/puqutogether/article/details/44587653
           if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)): #�������������������ԣ�ͬʱ���alphaֵ����֤�䲻�ܵ���0��C
              j = selectJrand(i,m) # ���ܴ�ʱ�����Ż�
              fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
              Ej = fXj - float(labelMat[j])
              alphaIold = alphas[i].copy()
              alphaJold = alphas[j].copy()
              if (labelMat[i] != labelMat[j]): # ��alpha������0-C֮��
                  L = max(0, alphas[j] - alphas[i])
                  H = min(C, C + alphas[j] - alphas[i])
              else:
                  L = max(0, alphas[j] + alphas[i] - C)
                  H = min(C, alphas[j] + alphas[i])
              if L==H: print("L==H"); continue
              eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T #�����޸���
              if eta >= 0: print("eta>=0"); continue # ���ETAΪ0����ô�����µ�alphas[j]�ͱȽ��鷳��
              alphas[j] -= labelMat[j]*(Ei - Ej)/eta
              alphas[j] = clipAlpha(alphas[j],H,L)
              # ���alpha[j]�Ƿ�����΢�ĸı䣬����ǵĻ������˳�forѭ����
              if (abs(alphas[j] - alphaJold) < 0.00001): print("j not moving enough"); continue
              # ��alpha[i], alpha[j]ͬ�����иı䣬�ı䷽��һ��
              alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])#update i by the same amount as j
                                                                  #the update is in the oppostie direction
              # �ڶ�alpha[i], alpha[j] �����Ż�֮�󣬸�������alphaֵ����һ������b��
              b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
              b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
              if (0 < alphas[i]) and (C > alphas[i]): b = b1
              elif (0 < alphas[j]) and (C > alphas[j]): b = b2
              else: b = (b1 + b2)/2.0
              alphaPairsChanged += 1
              print("iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged))
       # ��forѭ���⣬���alphaֵ�Ƿ����˸��£�����ڸ�����iter��Ϊ0��������г���
       if (alphaPairsChanged == 0): iter += 1
       else:iter = 0
       print("iteration number: %d" % iter)
   return b,alphas


def kernelTrans(X, A, kTup): # calc the kernel or transform data to a higher dimensional space
   """
   ��ת������
   Args:
       X:
       A:
       kTup: �˺�������Ϣ
   Returns:
   """
   m, n = shape(X)
   K = mat(zeros((m, 1)))
   if kTup[0] == 'lin':
       K = X * A.T # linear kernel
   elif kTup[0] == 'rbf':
       for j in range(m):
           deltaRow = X[j, :] - A
           K[j] = deltaRow * deltaRow.T
       K = exp(K / (-1 * kTup[1] ** 2)) # divide in NumPy is element-wise not matrix like Matlab
   else:
       raise NameError('Houston We Have a Problem -- \
   That Kernel is not recognized')
   return K


class optStruct:
   """
   ���������ݽṹ���������е���Ҫֵ
   """
   def __init__(self, dataMatIn, classLabels, C, toler, kTup): # Initialize the structure with the parameters
       """
       Args:
           dataMatIn:
           classLabels:
           C:
           toler:
           kTup: �����˺�����Ϣ��Ԫ��
       """
       self.X = dataMatIn
       self.labelMat = classLabels
       self.C = C
       self.tol = toler
       self.m = shape(dataMatIn)[0] # ���ݵ�����
       self.alphas = mat(zeros((self.m, 1)))
       self.b = 0
       self.eCache = mat(zeros((self.m, 2))) # ���棬��һ�и�������eCache�Ƿ���Ч�ı�־λ���ڶ��и�������ʵ�ʵ�Eֵ��
       self.K = mat(zeros((self.m, self.m)))
       for i in range(self.m):
           self.K[:, i] = kernelTrans(self.X, self.X[i, :], kTup)


def calcEk(oS, k):
   """
   ����Eֵ������
   �ù������������SMO�㷨������ִ����϶࣬��˽��䵥����Ϊһ������
   Args:
       oS:
       k:
   Returns:
   """
   fXk = float(multiply(oS.alphas, oS.labelMat).T * oS.K[:, k] + oS.b)
   Ek = fXk - float(oS.labelMat[k])
   return Ek


def selectJ(i, oS, Ei): # this is the second choice -heurstic, and calcs Ej
   """
   ��ѭ��������ʽ������
   ѡ��ڶ���(��ѭ��)alpha��alphaֵ
   �����Ŀ����ѡ����ʵĵڶ���alphaֵ�Ա�֤ÿ���Ż��в�����󲽳���
   �ú�����������һ��alphaֵEi���±�i�йء�
   Args:
       i:
       oS:
       Ei:
   Returns:
   """
   maxK = -1
   maxDeltaE = 0
   Ej = 0
   oS.eCache[i] = [1, Ei] # ���Ƚ�����ֵEi�ڻ��������ó�Ϊ��Ч�ġ��������Ч��ζ�����Ѿ�������ˡ�
   validEcacheList = nonzero(oS.eCache[:, 0].A)[0] # ����Eֵ����Ӧ��alphaֵ
   if (len(validEcacheList)) > 1:
       for k in validEcacheList: # �����е�ֵ�Ͻ���ѭ������ѡ������ʹ�øı������Ǹ�ֵ
           if k == i: continue # don't calc for i, waste of time
           Ek = calcEk(oS, k)
           deltaE = abs(Ei - Ek)
           if (deltaE > maxDeltaE):
              # ѡ�������󲽳���j
              maxK = k
              maxDeltaE = deltaE
              Ej = Ek
       return maxK, Ej
   else: # ����ǵ�һ��ѭ���������ѡ��һ��alphaֵ
       j = selectJrand(i, oS.m)
       Ej = calcEk(oS, j)
   return j, Ej


def updateEk(oS, k): # after any alpha has changed update the new value in the cache
   """
   �������ֵ�����뻺���С�
   �ڶ�alphaֵ�����Ż�֮����õ����ֵ��
   Args:
       oS:
       k:
   Returns:
   """
   Ek = calcEk(oS, k)
   oS.eCache[k] = [1, Ek]


def innerL(i, oS):
   """
   ��ѭ������
   Args:
       i:
       oS:
   Returns:
   """
   Ei = calcEk(oS, i)
   if ((oS.labelMat[i] * Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or (
       (oS.labelMat[i] * Ei > oS.tol) and (oS.alphas[i] > 0)):
       j, Ej = selectJ(i, oS, Ei) # this has been changed from selectJrand
       alphaIold = oS.alphas[i].copy()
       alphaJold = oS.alphas[j].copy()
       if (oS.labelMat[i] != oS.labelMat[j]):
           L = max(0, oS.alphas[j] - oS.alphas[i])
           H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
       else:
           L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
           H = min(oS.C, oS.alphas[j] + oS.alphas[i])
       if L == H:
           print("L==H")
           return 0
       eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j] # changed for kernel
       if eta >= 0:
           print("eta>=0")
           return 0
       oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
       oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
       updateEk(oS, j) # ��������
       if (abs(oS.alphas[j] - alphaJold) < 0.00001):
           print("j not moving enough")
           return 0
       oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j]) # update i by the same amount as j
       updateEk(oS, i) # ��������                  #the update is in the oppostie direction
       b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, i] - oS.labelMat[j] * (
       oS.alphas[j] - alphaJold) * oS.K[i, j]
       b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, j] - oS.labelMat[j] * (
       oS.alphas[j] - alphaJold) * oS.K[j, j]
       if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
           oS.b = b1
       elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
           oS.b = b2
       else:
           oS.b = (b1 + b2) / 2.0
       return 1
   else:
       return 0


def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
   """
   ����SMO�㷨��ѭ������smoSimple��Щ���ƣ��������ѭ���˳���������һЩ
   Args:
       dataMatIn:
       classLabels:
       C:
       toler:
       maxIter:
       kTup:
   Returns:
   """
   oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler, kTup)
   iter = 0
   entireSet = True
   alphaPairsChanged = 0
   while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
       alphaPairsChanged = 0
       if entireSet: # �����ݼ��ϱ������п��ܵ�alpha
           for i in range(oS.m):
               alphaPairsChanged += innerL(i, oS)
               print("fullSet, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
           iter += 1
       else: # �������еķǱ߽�alphaֵ��Ҳ���ǲ��ڱ߽�0��C�ϵ�ֵ��
           nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
           for i in nonBoundIs:
               alphaPairsChanged += innerL(i, oS)
               print("non-bound, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
           iter += 1
       if entireSet:
           entireSet = False # toggle entire set loop
       elif (alphaPairsChanged == 0):
           entireSet = True
       print("iteration number: %d" % iter)
   return oS.b, oS.alphas


def calcWs(alphas, dataArr, classLabels):
   """
   ����alpha����wֵ
   Args:
       alphas:
       dataArr:
       classLabels:
   Returns:
   """
   X = mat(dataArr)
   labelMat = mat(classLabels).transpose()
   m, n = shape(X)
   w = zeros((n, 1))
   for i in range(m):
       w += multiply(alphas[i] * labelMat[i], X[i, :].T)
   return w


def testRbf(k1=1.3):
   dataArr, labelArr = loadDataSet('testSetRBF.txt')
   b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf', k1)) # C=200 important
   datMat = mat(dataArr)
   labelMat = mat(labelArr).transpose()
   svInd = nonzero(alphas.A > 0)[0]
   sVs = datMat[svInd] # get matrix of only support vectors
   labelSV = labelMat[svInd]
   print("there are %d Support Vectors" % shape(sVs)[0])
   m, n = shape(datMat)
   errorCount = 0
   for i in range(m):
       kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', k1))
       predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
       if sign(predict) != sign(labelArr[i]): errorCount += 1
   print("the training error rate is: %f" % (float(errorCount) / m))
   dataArr, labelArr = loadDataSet('testSetRBF2.txt')
   errorCount = 0
   datMat = mat(dataArr)
   labelMat = mat(labelArr).transpose()
   m, n = shape(datMat)
   for i in range(m):
       kernelEval = kernelTrans(sVs, datMat[i, :], ('rbf', k1))
       predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
       if sign(predict) != sign(labelArr[i]): errorCount += 1
   print("the test error rate is: %f" % (float(errorCount) / m))


def img2vector(filename):
   returnVect = zeros((1, 1024))
   fr = open(filename)
   for i in range(32):
       lineStr = fr.readline()
       for j in range(32):
           returnVect[0, 32 * i + j] = int(lineStr[j])
   return returnVect


def loadImages(dirName):
   from os import listdir
   hwLabels = []
   print(dirName)
   trainingFileList = listdir(dirName) # load the training set
   m = len(trainingFileList)
   trainingMat = zeros((m, 1024))
   for i in range(m):
       fileNameStr = trainingFileList[i]
       fileStr = fileNameStr.split('.')[0] # take off .txt
       classNumStr = int(fileStr.split('_')[0])
       if classNumStr == 9:
           hwLabels.append(-1)
       else:
           hwLabels.append(1)
       trainingMat[i, :] = img2vector('%s/%s' % (dirName, fileNameStr))
   return trainingMat, hwLabels


def testDigits(kTup=('rbf', 10)):
   dataArr, labelArr = loadImages('trainingDigits')
   b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, kTup)
   datMat = mat(dataArr)
   labelMat = mat(labelArr).transpose()
   svInd = nonzero(alphas.A > 0)[0]
   sVs = datMat[svInd]
   labelSV = labelMat[svInd]
   print("there are %d Support Vectors" % shape(sVs)[0])
   m, n = shape(datMat)
   errorCount = 0
   for i in range(m):
       kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
       predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
       if sign(predict) != sign(labelArr[i]): errorCount += 1
   print("the training error rate is: %f" % (float(errorCount) / m))
   dataArr, labelArr = loadImages('testDigits')
   errorCount = 0
   datMat = mat(dataArr)
   labelMat = mat(labelArr).transpose()
   m, n = shape(datMat)
   for i in range(m):
       kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
       predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
       if sign(predict) != sign(labelArr[i]): errorCount += 1
   print("the test error rate is: %f" % (float(errorCount) / m))


'''#######********************************
Non-Kernel VErsions below
''' #######********************************


class optStructK:
   def __init__(self, dataMatIn, classLabels, C, toler): # Initialize the structure with the parameters
       self.X = dataMatIn
       self.labelMat = classLabels
       self.C = C
       self.tol = toler
       self.m = shape(dataMatIn)[0]
       self.alphas = mat(zeros((self.m, 1)))
       self.b = 0
       self.eCache = mat(zeros((self.m, 2))) # first column is valid flag


def calcEkK(oS, k):
   fXk = float(multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k, :].T)) + oS.b
   Ek = fXk - float(oS.labelMat[k])
   return Ek


def selectJK(i, oS, Ei): # this is the second choice -heurstic, and calcs Ej
   maxK = -1
   maxDeltaE = 0
   Ej = 0
   oS.eCache[i] = [1, Ei] # set valid #choose the alpha that gives the maximum delta E
   validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
   if (len(validEcacheList)) > 1:
       for k in validEcacheList: # loop through valid Ecache values and find the one that maximizes delta E
           if k == i: continue # don't calc for i, waste of time
           Ek = calcEk(oS, k)
           deltaE = abs(Ei - Ek)
           if (deltaE > maxDeltaE):
               maxK = k
               maxDeltaE = deltaE
               Ej = Ek
       return maxK, Ej
   else: # in this case (first time around) we don't have any valid eCache values
       j = selectJrand(i, oS.m)
       Ej = calcEk(oS, j)
   return j, Ej


def updateEkK(oS, k): # after any alpha has changed update the new value in the cache
   Ek = calcEk(oS, k)
   oS.eCache[k] = [1, Ek]


def innerLK(i, oS):
   Ei = calcEk(oS, i)
   if ((oS.labelMat[i] * Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or (
       (oS.labelMat[i] * Ei > oS.tol) and (oS.alphas[i] > 0)):
       j, Ej = selectJ(i, oS, Ei) # this has been changed from selectJrand
       alphaIold = oS.alphas[i].copy()
       alphaJold = oS.alphas[j].copy()
       if (oS.labelMat[i] != oS.labelMat[j]):
           L = max(0, oS.alphas[j] - oS.alphas[i])
           H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
       else:
           L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
           H = min(oS.C, oS.alphas[j] + oS.alphas[i])
       if L == H:
           print("L==H")
           return 0
       eta = 2.0 * oS.X[i, :] * oS.X[j, :].T - oS.X[i, :] * oS.X[i, :].T - oS.X[j, :] * oS.X[j, :].T
       if eta >= 0:
           print("eta>=0")
           return 0
       oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
       oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
       updateEk(oS, j) # added this for the Ecache
       if (abs(oS.alphas[j] - alphaJold) < 0.00001):
           print("j not moving enough")
           return 0
       oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j]) # update i by the same amount as j
       updateEk(oS, i) # added this for the Ecache                  #the update is in the oppostie direction
       b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[i, :].T - oS.labelMat[j] * (
       oS.alphas[j] - alphaJold) * oS.X[i, :] * oS.X[j, :].T
       b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[j, :].T - oS.labelMat[j] * (
       oS.alphas[j] - alphaJold) * oS.X[j, :] * oS.X[j, :].T
       if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
           oS.b = b1
       elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
           oS.b = b2
       else:
           oS.b = (b1 + b2) / 2.0
       return 1
   else:
       return 0


def smoPK(dataMatIn, classLabels, C, toler, maxIter): # full Platt SMO
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet: # go over all
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
                print("fullSet, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
            iter += 1
        else: # go over non-bound (railed) alphas
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                print("non-bound, iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
            iter += 1
            entireSet = False # toggle entire set loop
        elif alphaPairsChanged == 0:
            entireSet = True
        print("iteration number: %d" % iter)
    return oS.b, oS.alphas

if __name__ == "__main__":
   main()
