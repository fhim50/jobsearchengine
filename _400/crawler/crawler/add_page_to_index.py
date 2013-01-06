from add_to_index import Add_word_index
from bs4 import BeautifulSoup




class Index():
    def __init__(self):
        pass
    
    @staticmethod
    def add_page_to_index(index, url, content):
        page = BeautifulSoup(content)
        content = page.body.get_text()
        words = content.split()
        content_parsed=open('content_parse.txt','a')
		not_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for word in words:
			word = word.lstrip(not_char)
			word = word.rstrip(not_char)			
            
            content_parsed.write(word)
            
            Add_word_index.add_to_word_index(index, word, url)
        content_parsed.close() 
        return
