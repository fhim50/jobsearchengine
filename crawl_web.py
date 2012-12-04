'''
This is the crawler model that responsible for initiating the whole process to get the page that 
we want based on the seed urls that we have
'''

from union import Blend
from get_all_links import get_all_the_links
from get_page import get_content
from add_page_to_index import Index





class crawl():
    
    
    def __init__(self):
        pass
        
        
    @staticmethod   
    def crawl_web(seed):
            tocrawl=[seed]
            crawled=[]
            index=[]
            page=''
            while tocrawl:
                print 'processing ........'
                page = tocrawl.pop()
                if page not in crawled:
                        content=get_content.content_to_parse(page)
                        
                        Index.add_page_to_index(index, page, content)
                        Blend.mix(tocrawl,get_all_the_links.links(get_content.content_to_parse(page)))
                    
                        crawled.append(page)
                        
                        
            return crawled
        
crawl.crawl_web('http://joblistghana.com')

