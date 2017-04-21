#!/usr/bin/env python
#coding:utf8
'''
承上启下吧，在hadoop中，如果mapper端有接收到数据，并且给处理了，那么下个命令如果执行的reduce那么我们接受的
stdin就是来自于map
'''
import sys

word_count={}
lines = sys.stdin
for line in lines:
    word,count = line.split()#我们只要第一个单词，后面的1就不要了
    try:
        count = int(count)
        word_count[word] = word_count.get(word,0)+count
    except Exception:
        pass
list = sorted(word_count.items(),key=lambda item:item[1])
for m in list:
    print m[0]+"\t"+m[1]

