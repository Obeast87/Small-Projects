import urllib2

#Downloader
url = "http://littlegayblog.com"
page = urllib2.urlopen(url)
data = page.read()
print data

#Counter
print "The word gay was used %s times in this source." % data.index("gay")