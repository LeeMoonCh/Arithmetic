#coding:utf-8
from bs4 import  BeautifulSoup
import urllib
import re

file = open("E:\\1.csv","w")
url = "https://music.douban.com/tag/OST?start=0&type=T"
html = urllib.urlopen(url).read()
htmlformat = BeautifulSoup(html)
list = htmlformat.select("tr.item")
for tag in list:
    name = tag.find("a")["title"].replace(",","") 
    #print tag.find("div").find("div")
    ratings =  tag.find("div").find("div").select(".rating_nums")[0].text
    #print name
    pinglun =  re.search(r"[0-9]+", tag.find("div").find("div").select(".pl")[0].text).group()
    file.write("%s,%s,%s\n" %(name,ratings,pinglun))
file.close()
