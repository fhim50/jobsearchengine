class get_link():
    def __init__(self):
        pass
    @staticmethod
    def link(page):
            start_link = page.find('<a href=')
            if start_link == -1:
                return None, 0
            start_quote = page.find('"', start_link)
            end_quote = page.find('"', start_quote + 1)
            url = page[start_quote + 1:end_quote]
            return url, end_quote

