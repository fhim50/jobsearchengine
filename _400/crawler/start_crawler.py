#!usr/bin/env python2.7
from fetchpg import get_page
from indexpg import make_index
from get_all_links import links as all_links
from union import add_to_tocrawl

def crawl_web(seed):
    tocrawl = [seed]
    
    crawled = []
    index = {}
    while tocrawl:
        page_url = tocrawl.pop()
        if page_url not in crawled:
            content_soup ,base_robot_parsed_url= get_page(page_url)
            
            make_index(index, page_url, content_soup)
            outlinks=all_links(content_soup,base_robot_parsed_url)
            add_to_tocrawl(tocrawl, outlinks)
            crawled.append(page_url)
    return index

if __name__=='__main__':
     crawl_web('http://joblistghana.com')
else:
    pass