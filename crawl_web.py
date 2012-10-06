'''
This is the crawler model that responsible for initiating the whole process to get the page that 
we want based on the seed urls that we have
'''

from union import Blend
from get_all_links import get_all_the_links
from get_page import get_content





class crawl():
    
    
    def __init__(self):
        Blend.__init__(self)
        
        
    @staticmethod   
    def crawl_web(seed):
            tocrawl=[seed]
            crawled=[]
            page=''
            while tocrawl:
                page = tocrawl.pop()
                if page not in crawled:
                        Blend.mix(tocrawl,get_all_the_links.links(get_content.content_to_parse(page)))
                        tocrawl.append(page)
            return crawled
        
crawl.crawl_web('http://udacity.com')
