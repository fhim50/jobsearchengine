from urllib2 import urlopen,Request,URLError,HTTPError
import  robotexclusionrulesparser as parse_robot
from urlparse import urlparse ,urljoin
from bs4 import BeautifulSoup as soup

from responses import check_response

 
def get_page(url):
        try:
            
            parse_dict=urlparse(url)
            if parse_dict.scheme:
            
                base_url=parse_dict.scheme + '://'+ parse_dict.netloc
                robot_url=urljoin(base_url,'/robots.txt')
                parse_robot.user_agent='jocrawler 1.1'
            
                robot_parse=parse_robot.RobotFileParserLookalike()
            
                robot_parse.set_url(robot_url)
            
                
                robot_parse.read()
            
        
                if not robot_parse.can_fetch('jobcrawler 1.1', url):
                    print "This seed page can not be crawled based on robot.txt"
                    return soup(''),''
                
                else:
                    try:
                    
                        useragent='jobcrawler 1.1'
                        #headers={'User-Agent':useragent}
                        request=Request(url)
                        request.add_header('User-Agent', useragent)
                        response=urlopen(request)
                        if response.info().type not in ['text/html']:
                            return soup(''),''
                        the_page=response.read()
                        
                      
                        return soup(the_page),url
                    except URLError as connection_error:
                        print "Failed to reach server"
                        print 'Error code:',connection_error.code
                        
                    except HTTPError as _400_to_500:
                        print "The serve coudnot fulfill the request"
                        print 'Error code:',check_response(_400_to_500.code)
                    
                    else:
                        print 'EVERYTHING IS FINE'

        except URLError as connection_error:
             print 'FAILED TO REACH SERVER::'+url
             return soup(''),''
        except:
            print 'Check url again'+ url
            return soup(''),''
        
        #  print 'Error from fetchpg'
        
    
#we will write seperate models that will fetch urls fetch and insert into models

#print get_page('http://www.facebook.com/recover/initiate')      
            