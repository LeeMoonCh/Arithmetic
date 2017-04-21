# coding:utf8
import urllib
from bs4 import BeautifulSoup
url1 ="http://api.map.baidu.com/geocoder/v2/?address=北京市海淀区上地十街10号&ak=E4805d16520de693a3fe707cdc962045&callback=showLocation"

def getLoction(address):
    url = "http://api.map.baidu.com/geocoder/v2/?address=%s&ak=v9EPuFs4e4OvmXYlIRy0pIjeWceVvOz5&callback=showLocation"%(address)
    html = urllib.urlopen(url).read()
    bf = BeautifulSoup(html)
    return bf.find("lng").text,bf.find("lat").text


lng,lat = getLoction("北京市海淀区上地十街10号")
print "经度lng=>"+lng+"\n"+"维度lat=>"+lat

