#coding:utf8
# http://www.qiushibaike.com/8hr/page/2/
#div id = content-left 总盒子
#div class = article block untagged mb15 子盒子
#刚开始使用的urllib发现不能访问网页，故使用了urllib2的Request发送一个伪造报头

from bs4 import BeautifulSoup
import urllib
import urllib2
import re


'''
url = "http://www.qiushibaike.com"
获取到BeautifulSoup的一个实例
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
req = urllib2.Request(url,headers = headers )
html = BeautifulSoup(urllib2.urlopen(req).read())
通过id找到网页中的div盒子
divlist = html.select('#content-left')
#print len(divlist) #通过打印知道此列表只有一个元素
得到divlist中的元素，并且只去想要元素的div盒子
tags = divlist[0].select("div[class='article block untagged mb15']")
#便利tags得到每个tag
for tag in tags:
    print tag.select("div[class='author clearfix']")[0].select("h2")[0].text.encode("utf8")#获得段子发表者
    print tag.select(".contentHerf")[0].select("span")[0].text.encode("utf8")#获取段子内容
    #print tag
#通过得到下一页的span标签，得到它的父节点标签，父节点标签中含有下一页的链接。
newurl = divlist[0].select(".pagination")[0].select("span.next")[0].parent["href"]
'''   
'''以上分析结束  '''
#开始写方法
count = 1
url = "http://www.qiushibaike.com"
def getDuanzi(url,count):
    #打开一个新的文本
    file = open("e:\\out\\%d.txt" %(count),"w")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    req = urllib2.Request(url,headers = headers )
    html = BeautifulSoup(urllib2.urlopen(req).read())
    divlist = html.select('#content-left')
    tags = divlist[0].select("div[class='article block untagged mb15']")
    try:
        for tag in tags:            
            user =  tag.select("div[class='author clearfix']")[0].select("h2")[0].text.encode("utf8")#获得段子发表者
            print user
            content = tag.select(".contentHerf")[0].select("span")[0].text.encode("utf8")#获取段子内容
            file.write("%s\r\n%s\r\n\r\n" %(user,content))
        file.close()
        count+=1
        newurl = divlist[0].select(".pagination")[0].select("span.next")[0].parent["href"]
        url = "http://www.qiushibaike.com"+newurl
        getDuanzi(url,count)
    except Exception:
        pass
    
getDuanzi(url,count)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    