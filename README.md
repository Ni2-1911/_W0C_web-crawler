# _W0C_web-crawler
OVERVIEW
-
This is a basic CLI tool(command line interface) used for crawling a webpage in which URL and other information is given and we get output.
This project is done on python programming language.

REQUIREMENTS
-
for pythton modules - refer requirements.txt
other requirements - webDriver

Usage
-
python3 Main_Tool.py --h

python3 Main_Tool.py --e help

<img width="933" alt="Screenshot 2021-04-10 at 22 18 59" src="https://user-images.githubusercontent.com/79151737/114277884-c21efc00-9a4a-11eb-81ce-ea7bf657ba36.png">

Example
-
Suppose you have to find all headers of links to depth 1


python3 Main_Tool.py --e head --url https://youtube.com --depth 1

<img width="933" alt="Screenshot 2021-04-10 at 22 24 50" src="https://user-images.githubusercontent.com/79151737/114278097-b122ba80-9a4b-11eb-803e-42096ffcaa86.png">

to save your output in a file

python3 Main_Tool.py --e head --url https://youtube.com --depth 1 --edit save --path youtube/headers.txt

<img width="929" alt="Screenshot 2021-04-10 at 22 34 21" src="https://user-images.githubusercontent.com/79151737/114278327-eed41300-9a4c-11eb-95e1-a480ff597ac9.png">





