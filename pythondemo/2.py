import urllib2

try:
    req=urllib2.Request('http://192.168.191.130')
    res=urllib2.urlopen(req)
    print 'OK'
except urllib2.HTTPError as e:
    print e.code
except urllib2.URLError, e:
    print  e.reason
