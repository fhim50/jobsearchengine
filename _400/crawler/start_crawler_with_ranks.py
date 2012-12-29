#!usr/bin/env python2.7
from fetchpg import get_page
from indexpg import make_index
from get_all_links import links as all_links
from union import add_to_tocrawl

def crawl_web(seed):
    tocrawl = [seed]
    
    crawled = []
    index = {}
	graph = {}
    while tocrawl:
        page_url = tocrawl.pop()
        if page_url not in crawled:
            content_soup ,base_robot_parsed_url= get_page(page_url)
            
            make_index(index, page_url, content_soup)
            outlinks=all_links(content_soup,base_robot_parsed_url)
			graph[page_url] = outlinks
            add_to_tocrawl(tocrawl, outlinks)
            crawled.append(page_url)
    return index

if __name__=='__main__':
     crawl_web('http://joblistghana.com')
else:
    pass
	
def compute_ranks(graph):
	damping_factor = 0.8
	num_of_loops = 10
	ranks = {}
	number_of_pages = len(graph)
	for page in graph:
		ranks[page] = 1.0 / number_of_pages
	for i in range(0 , number_of_loops):
		newranks = {}
		for page in graph:
			newrank = (1 - dumping_factor )/  number_of_pages
		
			for node in graph:
			
				if page in graph[node]:
					newrank = newrank + dumping_factor * (ranks[node] / len(graph[node]))
			newranks[page] = newrank
		ranks = newranks
	return ranks 
	
	
	
#index , graph = crawl_web('http://www.xkcd.com')
#ranks = compute_ranks(graph)
#print ranks

'''
was not pushing
'''