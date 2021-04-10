import requests
from bs4 import BeautifulSoup
import sys
import re
import time
from termcolor import colored
import get_email
global ux  
ux=""

initial_time = time.time()
def get_links(u):
    global ux,x
    x=[]
    for links in u:
        try :
            if("http" not in links and "https" not in links and links[0]== "/" and links != ""):
                links=ux+links
            elif("http" not in links and "https" not in links and links[0] !="/" and links != ""):
                links=ux+"/"+links
        except TypeError :
            pass    
        task(links)

        try:
            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", 
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
                    "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
                    "Connection": "close", "Upgrade-Insecure-Requests": "1"}  
        
            response = requests.get(links, headers = header)
            soup = BeautifulSoup(response.text,'html.parser')

            for link in soup.find_all('a'):
                x.append(link.get('href'))
        except:
            pass

    return(x)

def task(task):

    try:
        print(get_email.get_source_code(task))
        print('WEBSITE: ' ,colored(task,'red'))
        print('TIME : ', colored(time.time() - initial_time,'blue'))

    except requests.exceptions.MissingSchema:
        pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
            
            
                

def get_depth(d,url):
    text=[]
    for i in range(d+1):
      url = get_links(url)


def get_url_depth(u ,d):
    url=[]
    url.append(u)
    ux=url[0]
    depth = int(d)
    get_depth(depth,url)


#example
get_url_depth('https://iitism.ac.in',1)



