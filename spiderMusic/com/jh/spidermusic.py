#coding:utf-8
from bs4 import BeautifulSoup
import urllib
import re
#0.准备io

#1.准备工作
url = "https://music.douban.com/tag/%E6%B0%91%E8%B0%A3"
html = urllib.urlopen(url).read()
formathtml = BeautifulSoup(html)
count = 1
def getMusic(url,count):
    
    file = open("D:\\xx\\%d.csv" %(count),"w")
    html = urllib.urlopen(url).read()
#2.获得一个BeautifulSoup的一个实例
    formathtml = BeautifulSoup(html)
#3.通过css选择器，找到自己想要的标签
    list =  formathtml.select("tr.item")
    try:
        for tag in list:
    #4.遍历list 得到每个元素，通过css选择器获得想要的标签，在通过find找到下级标签，最后得到这个下级
    #标签的title属性的值（这个值就是我们想要的内容）
            name = tag.select("div.pl2")[0].find("a")["title"]
            span_tag = tag.select("div[class='star clearfix']")[0].select("span.rating_nums")
            rating_nums = span_tag[0].text
            pl_tag = tag.select("div[class='star clearfix']")[0].select("span.pl")
            pl = pl_tag[0].text
    
            num = re.search(r"[0-9]+",pl).group()
            file.write("%s,%s,%s\n" %(name,rating_nums,num))
    except Exception:
        pass
    count +=1
    file.close()
    url = formathtml.select("span.next")[0].find("a")["href"]
    getMusic(url,count)
    

getMusic(url,count)