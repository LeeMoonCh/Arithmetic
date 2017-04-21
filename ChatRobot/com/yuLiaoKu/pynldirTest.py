# coding:utf8
import sys
import pynlpir

pynlpir.open() #使用pynlpir，这一步必须有
s = '海洋是如何形成的'
words = pynlpir.segment(s,pos_names='all',pos_english=False) #中文分词的函数
for word in words:
    print word[0]+"\t"+word[1] #查看分词结果
print 
words = pynlpir.get_key_words(s,weighted=True) #提取关键字，并且输出关键度
for word in words:
    print word[0],word[1]









