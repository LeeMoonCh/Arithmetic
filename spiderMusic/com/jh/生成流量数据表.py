#coding:utf-8
'''使用随机数来生成一张流量表'''

import random




file = open("E:\\1.txt","w")
for i in range(100000):
    phone = random.randint(138001,138999)

    upload = random.randint(0,1000)

    download = random.randint(0,1000)
    file.write("%d\t%d\t%d\n" %(phone,upload,download))
file.close()

