#!usr/bin/env python2.7
"""
/*
//     _ +------------------------------+ _
//    /o)|   Search Engine               |(o\
//   / / |       obeng william  & tk     | \ \
//  ( (_ |  _                         _  | _) )
// ((\ \)+-/o)-----------------------(o\-+(/ /))
// (\\\ \_/ /                         \ \_/ ///)
//  \      /                           \      /
//   \____/                             \____/
*/
"""

from fetchpg import get_page
from indexpg import make_index
from get_all_links import links as all_links
from union import add_to_tocrawl

def crawl_web(seed,mx_pg,mx_dp):
    tocrawl = [[seed,0]]
    
    crawled = []
    
    index = {}
    while tocrawl:
        
        page_url ,depth= tocrawl.pop(0)
        print 'This is the maximum number of pages crawled'+' '+str(len(crawled))
        print 'This is the DEPTH' , depth,page_url
    
        
        
        
        
        
        if (page_url not in crawled) and (len(crawled)< mx_pg) and (depth <=mx_dp):
            content_soup ,base_robot_parsed_url= get_page(page_url)
            
            make_index(index, page_url, content_soup)
            outlinks=all_links(content_soup,base_robot_parsed_url)
            add_to_tocrawl(tocrawl, outlinks,depth,crawled)
            crawled.append(page_url)
            
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            #yet to check for urls that contains urls that linked to the same pages
        
    return index

if __name__=='__main__':
      maximum_pages=1000
      maximum_depth=10
      crawl_web('http://joblistghana.com',maximum_pages,maximum_depth)
else:
    pass