from add_to_index import Add_word_index





class Index():
    def __init__(self):
        pass
    
    @staticmethod
    def add_page_to_index(index, url, content):
        words = content.split()
        content_parsed=open('content_parse.txt','a')
        for word in words:
            
            content_parsed.write(word)
            
            Add_word_index.add_to_word_index(index, word, url)
        content_parsed.close() 
        return