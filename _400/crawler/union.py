'''
This is the  union module that is responsible make sure to populate our tocrawl data structure with url to be crawled
It also makes sure that it does not duplicate the urls
'''
def add_to_tocrawl(to_crawl,outlinks,depth,crawled):
	try:
		for url in outlinks:
			if (url not in to_crawl):
				to_crawl.append([url,depth+1])
		
	except:
		print 'problem from union.add_tocrawl :check link'
			