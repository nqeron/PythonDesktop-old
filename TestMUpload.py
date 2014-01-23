import sys
import string
import gdata
import gdata.docs.service
def main(args):
    try:
        gd_client = gdata.docs.service.DocsService(source='NSF-uploadDoc-v2')
        gd_client.ssl = True
        gd_client.http_client.debug = False
        gd_client.ClientLogin('nqeron@gmail.com', 'themagician613')
        #help(gdata.MediaSource)
        for i in args:
            docFile = i
            try:
                spl = docFile.split("/")
                title = spl[len(spl)-1]
                spl = title.split(".")
                type = string.upper(spl[1])  #always in two parts
                print type
                print gdata.docs.service.SUPPORTED_FILETYPES[type]
                ms = gdata.MediaSource(file_path=docFile, content_type=gdata.docs.service.SUPPORTED_FILETYPES[type])
                    #spl = docFile.split("/")
                    #title = spl[len(spl)-1]
                entry = gd_client.Upload(ms, title)
                #s = str(entry.GetAlternateLink().href)
                #s = s.split("\n")[1]
                #s = "https:"+ s.split("https:")[1]
                print entry.GetAlternateLink().href
                #return 'Document now accessible online at:', s
            except IOError:
                print "Error: having file trouble with file "+ str(docFile)
                continue
                #return 'unsuccessful!'
    except:
        print "failed.  Check network connection!"
        return "failed"
    ##for i in args:
        ##print str(i) + "\n"
    return 0
if __name__=="__main__":
    input = sys.argv[1:][0]
    passt = input.split("Macintosh HD")
    main(passt)