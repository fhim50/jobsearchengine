from add_to_index import Add_word_index





class Index():
    def __init__(self):
        pass
    
    @staticmethod
    def add_page_to_index(index, url, content):
        words = content.split()
        for word in words:
            
            Add_word_index.add_to_word_index(index, word, url)
            
        return