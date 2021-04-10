#here code for get html in preetified form
import requests
from bs4 import BeautifulSoup


def get_source_code(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", "Upgrade-Insecure-Requests": "1"}  
    r = requests.get(url,headers = header)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    print(soup.prettify)

def get_page_text(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", "Upgrade-Insecure-Requests": "1"}  
    r = requests.get(url,headers = header)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    page_text = soup.get_text()
    print(page_text)

if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here
    get_page_text(url)
