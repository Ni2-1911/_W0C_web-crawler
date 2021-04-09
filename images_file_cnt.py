from bs4 import BeautifulSoup
import requests
import re
import _recurssion_


def get_img_cnt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    no_of_image = len(soup.find_all('img'))

    print("number of images : " ,no_of_image)

#add count number of pdfs


if __name__ == "__main__":
    url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here



