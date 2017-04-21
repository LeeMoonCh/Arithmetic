# coding:utf8
from numpy import *

l = mat(zeros((10,2)))

#l[1,:] = 1,2
listA = [[1,2,1],[1,2,3],[1,2,1],[3,2,1]]
print mat(listA)[:,0]
print "-----"
print nonzero((mat(listA)[:,0].A==3))
print nonzero((mat(listA)[:,0].A==3))[0]

