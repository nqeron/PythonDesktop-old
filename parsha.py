#!/usr/bin/env python
#import sys
import urllib2
import xml.dom.minidom
import HTMLParser
    

def parseFeed(feed):
	return xml.dom.minidom.parseString(feed)
def getParsha(document):
    item = document.getElementsByTagName("title")
    parsha = item[0]
    return parsha
def displayParsha(parsha):
     print "Parshat" + parsha.childNodes[0].data[19:]
    
feedURL = "http://www.chabad.org/tools/rss/parsha_rss.xml"
feed = urllib2.urlopen(feedURL).read()
document = parseFeed(feed);
if(document):
    parsha = getParsha(document)
    displayParsha(parsha)
else:
    print "Error parsing feed"