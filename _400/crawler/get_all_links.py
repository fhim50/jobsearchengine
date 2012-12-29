'''
This class is responsible for getting all links on the page 
making use of the class get_next_target class
'''


from urllib2 import urlopen
from bs4 import BeautifulSoup as soup
from seed import check_if_seed_hostname

from urlparse import urlparse,urljoin

def links(content_soup,url):
    links = []
    try:
        content_soup_all_a=content_soup.find_all('a')
        for a in content_soup_all_a:
            
            href=a.get('href')
        
            parse_url=urlparse(href)
            
            if href==None:
                pass
            elif href=="":
                pass
            elif parse_url.fragment and not parse_url.scheme:
                
                pass
            elif parse_url.scheme:
                if check_if_seed_hostname(parse_url):
                    links.append(str(href))
                    
                else:
                    
                    pass
                
                
                
            else:
                
                absolute_link=urljoin(url,str(href))
                links.append(absolute_link)
                
    except:
        print 'Error in get_all_links.py'+url
        return links
    links=list(set(links))
    return links

#c=urlopen('http://www.google.com')
#page=c.read();

#print links(soup(page),'http://www.google.com')