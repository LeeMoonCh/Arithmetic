#!coding:utf8

dictSet = set()
url = 'G:\\SogouR.reduced.txt'
fr = open(url)

for line in fr.readlines():
    listWords = line.split(',')
    listWords = listWords[0].split('-')
    for word in listWords:
        dictSet.add(word)

fw = open("G:\\listWords.txt",'w')
#for word in dictSet:
#    fw.write(word+"\n")
#建立索引，然后创建一个字典
dictIndex = {}
#dictSet = list(dictSet)
#print '我们走吧'[:3]
#print dictSet[0].encode('utf8')[0:3]
for word in dictSet:
    if word[:3] not in dictIndex.keys():
        dictIndex[word[:3]] = []
    dictIndex[word[:3]].append(word)

for key in dictIndex.keys():
    fw.write(key+'\n')
    for word in dictIndex[key]:
        fw.write(word+',')
    fw.write('\n')
fw.close()
fr.close()










