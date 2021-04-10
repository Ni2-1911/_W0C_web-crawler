# this is main File
import argparse
import os
import sys
import requests 
from selenium import webdriver
from bs4 import BeautifulSoup
from termcolor import colored

#python files
import _file_
import prettified_html_text
import take_screenshot
#import get_phone_numbers
import phone_depth
#import images_file_cnt
import img_cnt_depth
#import get_email
import email_depth
#import get_all_links
import _recurssion_
#import get_head
import get_headers



def find(args):
#url

    if args.e == "head" and args.edit == "save" :
        print(colored("Headers are getting saved in :  ",'blue')+colored( args.path ,'red'))
        sys.stdout = open(args.path, "w")
        get_headers.get_url_depth(args.url,args.depth)
        sys.stdout.close()
    elif args.e == "head" :
        get_headers.get_url_depth(args.url,args.depth)

        
    if args.e == "ss":
        take_screenshot.take_screenshot(args.url)
        print(colored("screenshot of this page is saved in current directory named :  ",'blue') + colored("main_page.png",'red' ))
        
    if args.e == "phone_no" and args.edit == "save":
        print(colored("phone_no are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        phone_depth.get_url_depth(args.url , args.depth)
        sys.stdout.close()
    elif args.e == 'phone_no':
        phone_depth.get_url_depth(args.url , args.depth)
    
    if args.e == "email" and args.edit == "save":
        print(colored("emails are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        email_depth.get_url_depth(args.url,args.depth)
        sys.stdout.close()
    elif args.e == 'email':
        email_depth.get_url_depth(args.url,args.depth)
        
    if args.e == 'link' and args.edit == 'save':
        print(colored("links are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        _recurssion_.get_url_depth(args.url ,args.depth )
        sys.stdout.close()
    elif args.e == 'link':
        _recurssion_.get_url_depth(args.url ,args.depth )

    if args.e == "cnt_image" and args.edit == "save":
        print(colored("data for number of images getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        img_cnt_depth.get_url_depth(args.url,args.depth)
        sys.stdout.close()
    elif args.e == 'cnt_image':
        img_cnt_depth.get_url_depth(args.url,args.depth)

    if args.e == "source_code" and args.edit == "save":
        print(colored("source code for this url getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        prettified_html_text.get_web_text(args.url)
        sys.stdout.close()
    elif args.e == 'source_code':
        prettified_html_text.get_web_text(args.url)
      
    if args.e == "web_text" and args.edit == "save":
        print(colored("web text data are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        prettified_html_text.get_source_code(args.url)
        sys.stdout.close()
    elif args.e == 'web_text':
        prettified_html_text.get_source_code(args.url)  

#files
    if args.create == "dir":
        _file_.create_project_dir(args.name)
        print(colored("directory created :  ",'blue')+colored( args.name,'red' ))
    
    if args.create == "txt":
        _file_.create_data_files(args.path ,args.name)
        print(colored("text file created  :  ",'blue')+colored( args.path,'red' ))

    if args.e == "help":
        print(colored("BASIC WEB CRAWLER WITH FOLLOWING FUNCTIONS: \n",'red')
                                    + colored("[head]        - give header of url  \n", 'green')
                                    + colored("[phone_no]    - give phone numbers in url \n", 'green')
                                    + colored("[cnt_image]   - count number of image in url \n", 'green')
                                    + colored("[email]       - give emails present in url \n" , 'green')
                                    + colored("[link]        - give links for any depth \n", 'green')
                                    + colored("[source_code] - give source code of given url \n", 'green')
                                    + colored("[web_text]    - give web text data of url \n", 'green')
                                    + colored("[ss]          - give take screen shot of given url \n", 'green'))


parser = argparse.ArgumentParser()
#arguments-url
parser.add_argument( '--e' , type = str, help = colored(" Enter: [head] / [ss] /[phone_no]/[cnt_image]/[email]/[link]/[source_code]/[web_text]/[help] ",'red'))
                                                                                  

parser.add_argument( '--url' , type = str, help = colored(" GIVE TARGET URL HERE ",'blue'))
parser.add_argument( '--depth' , type = int ,default=0 , help = colored(" GIVE DEPTH HERE   ",'blue') + colored(" deault value is 0",'red'))

#arguement-file
parser.add_argument( '--create' , type = str, help =colored('dir or txt file','blue' ))
parser.add_argument( '--name' , type = str, help =colored('enter file or directory name','blue' ))
parser.add_argument( '--path' , type = str, help =colored('enter path','blue' ))
parser.add_argument( '--edit' , type = str, help =colored('save your data to text file','blue'))

args = parser.parse_args()

sys.stdout.write(str(find(args)))


