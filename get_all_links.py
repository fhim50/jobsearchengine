'''
This class is responsible for getting all links on the page 
making use of the class get_next_targe class
'''
from get_next_target import get_link

class get_all_the_links(get_link):
    def __init__(self):
        pass
    
    
    @staticmethod
    def links(page):
        links = []
        print links
        while True:
            url, endpos = get_link.link(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                    break
        return links
