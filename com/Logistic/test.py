#coding:utf8
from numpy import *

listT = [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]]
listL = [[1],[2],[3],[4],[5]]
#print mat(listT)
#print mat(listL).transpose()

listT  = mat(listT)
listL = mat(listL)
m,n = shape(listT)
#print m,n
#print ones((n,1))
oneR = ones((n,1))
print ones(n)


h = 1.0/(1+exp(-listT*oneR))
#print h
#print listT*oneR
print listT.transpose()











