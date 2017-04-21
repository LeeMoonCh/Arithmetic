#!/usr/bin/env python
#coding:utf8
'''
sys系统库，内置的函数可以得到诸如参数等等，它的一个函数stdin,stdout，指的是标准输入和标准输出，在linux系统中，如果使用
echo命令像控制台打印一句话，这句话就可以在stdin中找到，所以，我的理解就是，其实他就是一个输入流。我们怎么操作输入流，就可以
怎么操作这个stdin。
'''
import sys

for line in sys.stdin:
    for m in line.split():
        print m,1

