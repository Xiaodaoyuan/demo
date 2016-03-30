# -*- coding=utf-8 -*-
import urllib2
import urllib
import re

class BDTB:
  
    def __init__(self,baseurl,seelz):
        self.baseurl = baseurl
        self.seelz = '?see_lz='+str(seelz)
     
    def getPage(self,pagenum):
        try:
            url = self.baseurl + self.seelz + '&pn='+ str(pagenum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None
     
    def getTitle(self,content):
        print content
        pattern = re.compile('<title>(.*?)</title>',re.S)
        result = re.search(pattern,content)
        print result
        if result:
           print result.group(1)
           return result.group(1)
        else:
           print 'None title'
           return None

baseurl = 'http://tieba.baidu.com/p/3138733512' 
bdtb = BDTB(baseurl,1)
content = bdtb.getPage(1)
title = bdtb.getTitle(str(content))
