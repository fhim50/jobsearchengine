from urlparse import urlparse

import csv
'''
This function receives input in the form of a parsed url and then return true or false if the url has the 
same hostname with those listed in our seed csv file..... 
'''

def check_if_seed_hostname(parse_url):
  try:
    
    if 'www' in parse_url.netloc.split('.'):
        parse_url_hostname=parse_url.netloc
    else:
        parse_url_hostname= 'www.' +'.'.join(parse_url.netloc.split('.'))
    with open('seeds.csv') as seeds:
        seeds_reader=csv.reader(seeds)
        for seedss in seeds_reader:
            
            for seed in seedss:
                
                seed_urlparse=urlparse(seed)
                
                if parse_url_hostname==seed_urlparse.netloc:
                    return True
                      
        return False
  except:
    print 'problem in seed.py'
                                      
    
  
#print check_if_seed_hostname(urlparse('http://joblistghana.com'))
 
           
    