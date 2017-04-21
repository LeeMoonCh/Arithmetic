#encoding:utf8

import time
fileIn = open("/opt/douban.csv")

lines = fileIn.readlines(5)
m = 1
while lines !=None:
    fileOut = open("/opt/testdata/flume/logs/"+str(m)+".csv","w")
    for line in lines:
        fileOut.write(line)
    print("/opt/testdata/flume/logs/"+str(m)+".csv",",over")
    m =m+1
    time.sleep(5)
    fileOut.close()
    lines = fileIn.readlines(5)
fileIn.close()   