#coding:utf8
import pickle
def getMydict(filename):
    dictSet = set()
    fr = open(filename)
    for line in fr.readlines():
        listWords = line.split(',')
        listWords = listWords[0].split('-')
        for word in listWords:
            dictSet.add(word)
    
    dictIndex = {}
    for word in dictSet:
        if word[:3] not in dictIndex.keys():
            dictIndex[word[:3].encode('utf8')] = []
        dictIndex[word[:3].encode('utf8')].append(word.encode('utf8'))
    return dictIndex


#dict = getMydict('G:\\SogouR.reduced.txt')
def saveData(data,filename):
    fw = open(filename,"w")
    pickle.dump(data, fw)
    fw.close()
#加载树   
def loadData(filename):
    fw=open(filename)
    return pickle.load(fw) 

#saveData(dict, "G:\\myDict")

dict = loadData("G:\\myDict")

def participle(data,str):
    returnStr =""
    strR = ""
#    print len(str)
    if len(str)>0:
        try:
            
            for key in data.keys():
                if str[:1] == key:
                    for i in range(4):
                        for word in data[key]:
                            if len(str)>=4:
                                m = i+1
                                if str[0:m] == word:
                                    strR = word.decode("utf8")
                    break  
                else:strR = str[:1]
        except Exception:
            pass
#        print len(strR)
#        print strR
        returnStr +=strR+"  "
#        print returnStr
        strL = str[len(strR):]
#        print len(strL)
#        print '~~~'
        if len(strL)>0:
            returnStr += participle(data,strL)
    return returnStr
#str = '我是一个中国人,也是一个学生'
#print str.encode('utf8')[8:]
print participle(dict,u'我是中国人,也是个学生')
#print len('哈哈'.decode('utf-8')) #unicode格式
#print len('哈哈') #utf-8格式

#str = '中国人'
#strR = ""
#for key in dict.keys():
#    if str[:3] == key:
#        for i in range(4):
#            for word in dict[key]:
#                m = (i+1)*3
#                if str[0:m] == word:
#                    strR = word
#                    print strR
#print strR













