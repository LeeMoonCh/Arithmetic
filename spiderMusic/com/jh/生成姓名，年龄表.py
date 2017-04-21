#coding:utf8

import random


file = open("E:/people.txt","w")
for m in range(10000):
    name1 = random.choice(["李","闫","白","邢","田","赵","王"])
    name2 = random.choice(["A","B","C","D","E","F","G","H"])
    age = random.randint(18,32)
    
    file.write(name1+name2+","+str(age)+"\r")
file.close()


