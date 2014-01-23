#!/usr/bin/env python
#import sys
import urllib2
import xml.dom.minidom
import HTMLParser
    

#def get_from_blogama():
  #url = "http://blogama.org/ip_query.php?output=xml&ip="
  #rawData = ""
  #try:
    #rawData = urllib.urlopen(url).read()
    #dom = minidom.parseString(rawData)
    #print_blogama(dom)
  #except:
    #print "Couldn't parse dmw output"
    #print rawData
    #return

#def print_blogama(dom):
    #countryCode = dom.getElementsByTagName("CountryCode").item(0).childNodes[0].nodeValue
    #zipCode = dom.getElementsByTagName("ZipPostalCode").item(0).childNodes[0].nodeValue
    #print countrCode + zipCode
    
    
#if __name__ == "__main__":
    #ip = sys.argv[1]
    #get_from_blogama()
    
def parseFeed(feed):
	return xml.dom.minidom.parseString(feed)
def getTimes(document):
    item = document.getElementsByTagName("title")
    return item
def displayTimes(times):
    print times[0].childNodes[0].data + "\n"+ "\n"
    for time in times[1:]:
        print time.childNodes[0].data[:-15] + "\n"
        
zipcode = "07006" #home
#zipcode = "02454" #brandies
feedURL = "http://www.chabad.org/tools/rss/zmanim.xml?z="+zipcode
feed = urllib2.urlopen(feedURL).read()
document = parseFeed(feed);
if(document):
    times = getTimes(document)
    displayTimes(times)
else:
    print "Error parsing feed"