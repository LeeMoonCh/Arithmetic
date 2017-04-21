# coding:utf8
import pickle
fr = open("dict.txt")
#fw = open("set.txt","w") 
dictSet = set()
dict = {}
for line in fr.readlines():
    words = line.strip().split("\t")
    words = words[0].split('-')
    
    for word in words:
        dictSet.add(word) 
        
for word in dictSet:
    if word[:3] not in dict.keys():
        dict[word[:3]] = []
    dict[word[:3]].append(word)

def saveDate(data,filename):
    fw = open(filename,"w")
    pickle.dump(data, fw)
    fw.close()
    
saveDate(dict,"set.txt")    
    
    
    
    
    
    
#        print word


