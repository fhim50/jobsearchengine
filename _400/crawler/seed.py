from urlparse import urlparse

import csv

def check_if_seed_hostname(parse_url):
    with open('seeds.csv') as seeds:
        seeds_reader=csv.reader(seeds)
        
        for seedss in seeds_reader:
            
            for seed in seedss:
                
                seed_urlparse=urlparse(seed)
                
                print (seed_urlparse.netloc,parse_url.netloc)
                if parse_url.netloc==seed_urlparse.netloc:
                    print 'a'
                    return True,
                      
        return False
                                      
    
  
print check_if_seed_hostname(urlparse('http://wwww.joblistghana.org'))
 
           
    