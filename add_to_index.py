class Add_word_index():
    def __init__(self):
        pass
    
    @staticmethod
    def add_to_word_index(index, keyword, url):
        for entry in index:
            if entry[0] == keyword:
                entry[1].append(url)
                return
            # not found, add new keyword to index
            index.append([keyword, [url]])
            
        return 

