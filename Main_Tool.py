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
import get_phone_numbers
import images_file_cnt
import prettified_html_text
import take_screenshot
import get_head
import get_all_links
import sys
import get_email
import _recurssion_



def find(args):
#url
    if args.e == "head":
        get_head.get_headers(args.url)
    if args.e == "head" and args.edit == "save":
        print(colored("Headers are getting saved in :  ",'blue')+colored( args.path ,'red'))
        sys.stdout = open(args.path, "w")
        get_head.get_headers(args.url)
        sys.stdout.close() 

    if args.e == "ss":
        print(colored("screenshot of this page is saved in current directory",'blue'))
        take_screenshot.take_screenshot(args.url)

    if args.e == "link_d1":
        get_all_links.get_links(args.url)
    if args.e == "link_d1" and args.edit == "save":
        print(colored("links of depth_1 are getting saved in :  ",'blue')+ colored( args.path ,'red'))
        sys.stdout = open(args.path, "w")
        get_all_links.get_links(args.url)
        sys.stdout.close() 
        
    if args.e == 'phone_no':
        get_phone_numbers.get_phone(args.url)
    if args.e == "phone_no" and args.edit == "save":
        print(colored("phone_no are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        get_phone_numbers.get_phone(args.url)
        sys.stdout.close() 
    
    if args.e == 'email':
        get_email.get_source_code(args.url)
    if args.e == "email" and args.edit == "save":
        print(colored("emails are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        get_email.get_source_code(args.url)
        sys.stdout.close() 

    if args.e == 'link':
        _recurssion_.get_url_depth(args.url ,args.depth )
    if args.e == 'link' and args.edit == 'save':
        print(colored("links are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        _recurssion_.get_depth(args.url ,args.depth )
        sys.stdout.close()

    if args.e == 'cnt_image':
        images_file_cnt.get_img_cnt(args.url)
    if args.e == "cnt_image" and args.edit == "save":
        print(colored("data for number of images getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        images_file_cnt.get_img_cnt(args.url)
        sys.stdout.close() 

    if args.e == 'source_code':
        prettified_html_text.get_source_code(args.url)
    if args.e == "source_code" and args.edit == "save":
        print(colored("source code for this url getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        prettified_html_text.get_source_code(args.url)
        sys.stdout.close() 

    if args.e == 'web_text':
        prettified_html_text.get_source_code(args.url)        
    if args.e == "web_text" and args.edit == "save":
        print(colored("web text data are getting saved in :  ",'blue')+colored( args.path,'red' ))
        sys.stdout = open(args.path, "w")
        prettified_html_text.get_source_code(args.url)
        sys.stdout.close() 

#files
    if args.create == "dir":
        _file_.create_project_dir(args.name)
        print(colored("directory created :  ",'blue')+colored( args.name,'red' ))
    
    if args.create == "txt":
        _file_.create_data_files(args.path ,args.name)
        print(colored("text file created  :  ",'blue')+colored( args.path,'red' ))


parser = argparse.ArgumentParser()

#arguments-url
parser.add_argument( '--e' , type = str, help = colored(" Enter: [head] / [ss] / [link_d1]/[phone_no]/[cnt_image]/[email]/[link]/[source_code]/[web_text] ",'red')
                                                            + colored("[head] - give header of url", 'green')
                                                            + colored("[link_d1] - links for depth1  of url", 'green')
                                                            + colored("[phone_no] - give phone numbers in given url", 'green')
                                                            + colored("[cnt_image] - count number of image in givel url", 'green')
                                                            + colored("[email] - give emails present in given url", 'green')
                                                            + colored("[link] - give links for any depth", 'green')
                                                            + colored("[source_code] - give source code of url", 'green')
                                                            + colored("[web_text] - give web text data of url", 'green')
                                                            + colored("[ss] - give take screen shot", 'green'))
                            

parser.add_argument( '--url' , type = str, help = colored(" give target url here ",'blue'))
parser.add_argument( '--depth' , type = int ,default=0 , help = colored(" GIVE DEPTH HERE (by default it will take 0)",'blue') + colored(" will only take for [link] ",'red'))

#arguement-file
parser.add_argument( '--create' , type = str, help =colored('directory or txt file','blue' ))
parser.add_argument( '--name' , type = str, help =colored('enter file or directory name','blue' ))
parser.add_argument( '--path' , type = str, help =colored('enter path','blue' ))
parser.add_argument( '--edit' , type = str, help =colored('save your data to text file','blue'))

args = parser.parse_args()

sys.stdout.write(str(find(args)))

