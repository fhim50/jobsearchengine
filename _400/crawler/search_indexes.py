def add_to_search_index(index,keyword,url):
  try:
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]
    
  except:
      print 'problem from search indexes'