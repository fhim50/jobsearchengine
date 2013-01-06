'''
This is the crawler model that responsible for initiating the whole process to get the page that 
we want based on the seed url that is given.
'''

from union import Blend
from get_all_links import get_all_the_links
from get_page import get_content
from add_page_to_index import Index





class crawl():
    
    
    def __init__(self):
        pass
        
        
    @staticmethod   
    def crawl_web(seed,max_pages):
            '''
            tocrawl is a data structure that contains all urls to be crawled.
            crawled is a also data structure that contains all urls already crawled.
            '''
            tocrawl=[seed]
            crawled=[]
            index=[]
            '''
            page contains the next url to be crawled.
            '''
            page=''
            while tocrawl:
                print 'processing ........'
                page = tocrawl.pop()
                if page not in crawled and len(tocrawl)<=max_pages:
                        content=get_content.content_to_parse(page)
                        print len(tocrawl)
                        Index.add_page_to_index(index, page, content)
                        Blend.mix(tocrawl,get_all_the_links.links(get_content.content_to_parse(page)))
                    
                        crawled.append(page)
                        
                        
            return crawled,'max page reached'
        
print crawl.crawl_web('http://joblistghana.com',10)

