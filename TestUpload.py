import sys
import string
import gdata
import gdata.docs.service

def main(args):
    docFile = args[0]
    try:
        gd_client = gdata.docs.service.DocsService(source='NSF-uploadDoc-v1')
        gd_client.ssl = True
        gd_client.http_client.debug = False
        gd_client.ClientLogin('nqeron@gmail.com', 'themagician613')
            #help(gdata.MediaSource)
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
            return 'Document now accessible online at:', s
        except IOError:
            print "Error: having file trouble"
            return 'unsuccessful!'
    except:
        print "failed.  Check network connection!"
        return "failed"
    ##except socket.gaierror:
        ##return "no connection"
if __name__=="__main__":
    main(sys.argv[1:])