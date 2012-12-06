'''
This is the  union module that is responsible make sure to populate our tocrawl data structure with url to be crawled
It also makes sure that it does not duplicate the urls
'''
class Blend():
	def __init__(self):
		pass
	@staticmethod
	def mix(to_crawl, all_links_on_page):
		for url in all_links_on_page:
			if url not in to_crawl:
				to_crawl.append(url)
			