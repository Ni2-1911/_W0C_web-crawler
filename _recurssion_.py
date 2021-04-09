import requests
from bs4 import BeautifulSoup
import sys
import re
import time
from termcolor import colored
global ux   
ux=""

initial_time = time.time()
def get_links(u):
    global ux,x
    x=[]
    for links in u:
        if("http" not in links and "https" not in links and links[0]== "/" and links != ""):
            links=ux+links
        elif("http" not in links and "https" not in links and links[0] !="/" and links != ""):
            links=ux+"/"+links
        response = requests.get(links)
        soup = BeautifulSoup(response.text,'html.parser')
        for link in soup.find_all('a'):
            x.append(link.get('href'))

    print(x)
    print("no of links we get: " , len(x))
    print("time :" , colored (time.time() - initial_time,'red'))
    return(x)

def get_depth(d,url):
    text=[]
    if d==0:
        print(url)
    elif d>0:
        for i in range(d):
            url = get_links(url)
    else: 
        print(colored("PLEASE ENTER A VALID DEPTH ",'red'))

def get_url_depth(u ,d):
    url=[]
    url.append(u)
    ux=url[0]
    depth = int(d)
    get_depth(depth,url)


#example
#get_url_depth('https://google.com',1)



