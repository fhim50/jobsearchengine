from urllib2 import urlopen

class get_content():
    
    
    @staticmethod
    def content_to_parse(url):
        try:
            a=urlopen(url)
            page=a.read()
            return page
        except:
            return "can not access the web"
        return ""
            