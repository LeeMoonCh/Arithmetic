# coding:utf8
import pickle
fw = open("keyValue.txt","w")
fr = open("set.txt")
dict = pickle.load(fr)

#for key in dict.keys():
#    fw.write(key+":")
#    for word in dict[key]:
#        fw.write(word+",")
#    fw.write("\n")
#        
#fw.close()

def participle(data,s):
    s = s.decode("utf8")
    strR = ""
    for key in data.keys():
        if s[:1]==key:
            for i in range(4):
                if s[:i+1] in data[key]:
                    strR =s[:i+1]
            break
        else:
            strR=s[:1]
    s = s[len(strR):]
    
    if len(s)>0:
        strR+=" "+participle(data,s)
#        print strR
    return strR
    
    
    
print participle(dict,"我要让爸爸抬起头，练好技术争取年薪20万")    
    
    
    
    













