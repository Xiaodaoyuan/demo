# -*- coding=utf-8 -*-
import urllib2
import urllib
import re


class Spider:
    def __init__(self,baseurl):
       self.baseurl = baseurl

    def getPage(self,pageNum):
        try:
           url = self.baseurl + '?page=' + str(pageNum)
           request = urllib2.Request(url)
           response = urllib2.urlopen(request)
           return response.read().decode('gbk')
        except:
           return None
 
    def getContents(self,pageNum):
        content = self.getPage(pageNum)
        pattern = re.compile('<div class="list-item">.*?pic-word.*?<img src="(.*?)" alt.*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        result = re.finditer(pattern,content)
        for m in result:
           print m.group(1),m.group(2),m.group(3),m.group(4)
        return result

spider = Spider('http://mm.taobao.com/json/request_top_list.htm')
spider.getContents(1)
          
