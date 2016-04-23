import urllib2
x = raw_input("URL: ")
y = raw_input("Word to count: ")

#Downloader
url = x
page = urllib2.urlopen(url)
data = page.read()
print data

#Counter
print "The word %s was used %s times in this source." % (y, data.count(y))
