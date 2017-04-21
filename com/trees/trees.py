#!coding:utf8
import pickle
from math import log
from numpy import array
import operator
from com.trees.TreePlot import createPlot
from matplotlib.transforms import MINFLOAT

def getMore(classList):
    dict = {}
    for key in classList:
        if key not in dict.keys():
            dict[key] = 0
        dict[key] +=1
    sortedDict = sorted(dict.iteritems(),key = operator.itemgetter(1),reverse = True)
    return sortedDict[0][0]

def getGain(dataSet):
    #首先思考，数据集传进来，我们需要得到一个每个分类出现的概率
    #取到dataSet的长度，用于计算分类在数据集中出现的概率
    x = len(dataSet)
    dict = {}
    for dataset in dataSet:
        #取到数据集的最后一位，我们传dataSet时要按照这个标准来进行约束，最后一个必须是分类。
        key = dataset[-1]
        if key not in dict.keys():
            dict[key] = 0
        dict[key]+=1
        #以上代码代表着，计算每个分类在此数据集中出现的个数。我们使用字典来进行累加计算
#    print dict
    f = 0.0
    for key1 in dict.keys():
        #得到了每一个分类在数据集中出现的概率
        p = float(dict[key1])/x
#        print p
        #按照公式开始导入
        f -= p*log(p,2)
    return f
#通过测试发现-1是取数据集的最后一个
#list =[[1,1,"yes"],[1,1,"yes"],[1,0,"no"],[0,1,"no"],[0,1,"no"]]
#dataSet1 = array(list)
##print dataSet1
#f =  getGain(dataSet1)
#print f
list = [['young', 'myope', 'no', 'reduced', 'no lenses'], ['young', 'myope', 'no', 'normal', 'soft'], ['young', 'myope', 'yes', 'reduced', 'no lenses'], ['young', 'myope', 'yes', 'normal', 'hard'], ['young', 'hyper', 'no', 'reduced', 'no lenses'], ['young', 'hyper', 'no', 'normal', 'soft'], ['young', 'hyper', 'yes', 'reduced', 'no lenses'], ['young', 'hyper', 'yes', 'normal', 'hard'], ['pre', 'myope', 'no', 'reduced', 'no lenses'], ['pre', 'myope', 'no', 'normal', 'soft'], ['pre', 'myope', 'yes', 'reduced', 'no lenses'], ['pre', 'myope', 'yes', 'normal', 'hard'], ['pre', 'hyper', 'no', 'reduced', 'no lenses'], ['pre', 'hyper', 'no', 'normal', 'soft'], ['pre', 'hyper', 'yes', 'reduced', 'no lenses'], ['pre', 'hyper', 'yes', 'normal', 'no lenses'], ['presbyopic', 'myope', 'no', 'reduced', 'no lenses'], ['presbyopic', 'myope', 'no', 'normal', 'no lenses'], ['presbyopic', 'myope', 'yes', 'reduced', 'no lenses'], ['presbyopic', 'myope', 'yes', 'normal', 'hard'], ['presbyopic', 'hyper', 'no', 'reduced', 'no lenses'], ['presbyopic', 'hyper', 'no', 'normal', 'soft'], ['presbyopic', 'hyper', 'yes', 'reduced', 'no lenses'], ['presbyopic', 'hyper', 'yes', 'normal', 'no lenses']]
list = array(list)

#print list
#print list[0]
#for dataset in list:
#    print dataset[1]

def splitDataSet(dataSet,index):
    #对某一个特征进行分类
    dict = {}
    #遍历此数据集
    for dataLine in dataSet:
        #取得数据集对应下标的特征值，并加入字典。
        value = dataLine[index]
        if value not in dict.keys():
            dict[value] = 1
        #这样子我们就将这个特征的所有值进行了汇合。
#    print dict.keys()
    #遍历字典的所有key，每次进入一个新的key时，将listA和listE直空。
    for key in dict.keys():
        listA=[]
        listE = []
        #再次遍历数据集
        for dataLine in dataSet:
            #判断数据的特征值是否和key相等，如果相等，将listE制空
            if dataLine[index] == key:
                listE = []
                #循环数据长度，在循环中判断i是否是特征下标，如果不是，将i对应的特征值加入listE，然后循环结束后，将listE加入listA
                for i in range(len(dataLine)):
                    if i is not index:
                        listE.append(dataLine[i])
                listA.append(listE)
        #每个key对应的listA。
        dict[key] = listA
    return dict

#print splitDataSet(list, 1)
#选择最好的数据划分方式
def chooseBest(dataSet):
    #获得原始数据集的期望值
    oldGain = getGain(dataSet)
#    print oldGain
    x = -10
    
    #遍历所有特征，得到每个特征的字典。
    for i in range(len(dataSet[0])):
        dict = splitDataSet(dataSet,i)
#        print dict
        newGain = 0.0
        for keyM in dict.keys():
#            print keyM
            
#            print dict[keyM]
            #获取每个特征的每个分类在数据集中的概率。
            p = float(len(dict[keyM]))/len(dataSet)
#            print p
#            print getGain(dict[keyM])
            #将每个特征的分类期望值相加，得到这个特征的总期望值。
            newGain += p*getGain(dict[keyM])
#            print newGain
        #然后将原始数据集的期望值-新的期望值，得到一个相对期望
        infoGain = newGain - oldGain
       
        #设置一个期望值为0.0的变量，如果相对期望大于0.0，将此变量重新赋值成infoGain
        
#        print infoGain
#        print '~~'
        if infoGain>x:
            x = infoGain
            bestFuture = i
    return bestFuture
            

#classList = [m[-1] for m in list]
#print classList.count(classList[0])
#print list[0]
#print chooseBest(list)

def createTree(dataSet,labels):
    #classList是dataSet每行的最后一个特征值
    classList = [x[-1] for x in dataSet]
    #第一个停止条件为：类别完全相同，停止。怎么代表类别完全相同，当classList的第一个元素的总数和classList的总长度一样时。
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #第二个停止条件是，当dataSet的长度是1的时候，也就是说所有特征都走了一遍，还没有发现第一个停止条件，我们返回classList中出现次数最多的类别
    if len(dataSet) == 1:
        return getMore(classList)
    #获得最佳特征的下标
    bestIndex = chooseBest(dataSet)
    #获取对应的特征标签
    bestLabel = labels[bestIndex]
    print bestIndex
    print bestLabel
    myTree = {bestLabel:{}}
    print myTree
    print "!"*50
    del(labels[bestIndex])
    #获取到最佳分类字典
    dict = splitDataSet(dataSet, bestIndex)
    #遍历这个最佳分类字典
    for key in dict.keys():
        myTree[bestLabel][key] = createTree(dict[key],labels[:])
    return myTree

listM = ['A','B','C','D']
inTree = createTree(list,listM)
#m = inTree.keys()[0]
#listM = ['A','B']
print inTree
#print inTree[m]
#print listM.index(m) 
#createPlot(inTree)

def classify(dataTree,labels,testData):
    #取得决策树的第一个key值
    firstStr = dataTree.keys()[0]
#    print firstStr
    #获得第二个决策树，当作递归的参数
    secondTree = dataTree[firstStr]
#    print secondTree
    indexLabels = labels.index(firstStr)
#    print indexLabels
#    print testData[indexLabels]
#    print secondTree.keys()
    classLabel = "无法估测"
    #通过firstStr得到labels中相对应的下标
    for key in secondTree.keys():
        if key == str(testData[indexLabels]):
            if type(secondTree[key]).__name__=='dict':
                classLabel = classify(secondTree[key],labels,testData)
            else:
                classLabel = secondTree[key]
    return classLabel
#listM = ['A','B']
#print classify(inTree, listM, [0,0])
#print str("enen")           
#存储树    
def saveTree(dataTree,filename):
    fw = open(filename,"w")
    pickle.dump(dataTree, fw)
    fw.close()
#加载树   
def loadTree(filename):
    fw=open(filename)
    return pickle.load(fw) 

#saveTree(inTree,"E:\\a.txt")
#print loadTree('E:\\a.txt')
    












