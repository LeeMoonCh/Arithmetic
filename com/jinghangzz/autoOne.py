#!coding:utf8


#传入动态参数为list表
def autoOne(*lists):
    #获取动态参数的长度
    num = len(lists)
    listMins = []
    listn=[]
    for i in range(num):
        maxs = max(lists[i])
        mins = min(lists[i])
        n = maxs - mins
        #将每个数组的最小值和极差放入一个数组中
        listMins.append(float(mins))
        listn.append(float(n))
        list1 = lists[i]
        lens = len(list1)
        for j in range(lens):
            list1[j] = (float(list1[j]-mins))/n
    return listMins,listn
#测试通过
listTest1 = [1.0,2.0,3.0,4.0,5.0,100.0]
listTest2 = [100,200,244,666,108] 
#autoOne(list2,list3)
#print list2
#print list3
#对测试数据进行归一
def testAutoOne(listMins,listn,list):
    num = len(list)
    for i in range(num):
        list[i] = (float(list[i])-float(listMins[i]))/float(listn[i])
    return list
##测试通过
#list = [1.3,101]
#list1,list2 = autoOne(listTest1,listTest2)
#print listTest1
#print listTest2
#
#testAutoOne(list1, list2, list)
#print list






















