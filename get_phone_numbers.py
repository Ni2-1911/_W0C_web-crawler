#get website text
import requests
from bs4 import BeautifulSoup
import re
import _file_

def get_phone(url):
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    page_text = soup.get_text()
    
    
    a = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', page_text)
    print(a)




if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE - ") # --enter url
    get_phone(url)