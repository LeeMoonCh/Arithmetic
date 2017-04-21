import sys  
sys = reload(sys)  
sys.setdefaultencoding('utf8')



def on_start(self):
    
    no = 1
    while no<=30:
        
        url = 'http://www.lanrentuku.com/s.php?keyword=%C3%C0%C5%AE&PageNo='+str(no)
        self.crawl(url, callback=self.index_page)
        no += 1
        print url