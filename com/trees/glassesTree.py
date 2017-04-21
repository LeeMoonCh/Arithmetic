#!coding:utf8
from numpy import array
from com.trees.tressBook import createTree
from com.trees.TreePlot import createPlot

fr = open("G:\\1.txt")
listL = [line.strip().split("\t") for line in fr.readlines()]
#for line in fr.readlines():
#    listL.append(line.strip().split("\t"))

listA = ['age','prescript','astigmatic','tearTate']

inTree = createTree(listL,listA)
print inTree

createPlot(inTree)





