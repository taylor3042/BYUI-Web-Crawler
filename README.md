# BYUI-Web-Crawler

Author: Taylor Peterson

Purpose: Detecting and exporting info from BYUI help guides 

## Prerequisites

In order to run this software, you will need to have pthon 10 or greater installed. Using python's installer pip, you will need to install beautiful soup by using the command: pip install beautifulsoup4. You will also need to most likely install request by using the command: pip install requests

Depending on your Operating System (Windows, Linux, Apple), you will need to run this with python in your terminal. It would look something like this: python helpguide_crawler.py inside powershell, commandprompt or the terminal of apple/linux machine. If you have Visual Studio Code editor (or another similar code editor) you can click the play button instead.

## Usage
Run the python file helpguide_crawler.py to run all python files together. No arguments are needed if you want to run the default settings. The settings to choose from are:

### Help:
This will pull up the help and usage, most will be found below. No arguments are given.

Example Usage: python helpguide_crawler.py --help 

### Rerun:
This is going to re-run the scanner. It's suggested you do this everytime to make sure it can catch all the possible articles. The arguments are True and False. The default is set to True.

Example Usage: python helpguide_crawler.py --rerun False

### Scan:
This specifies wether you would like a deep scan or shallow scan. Note: deep scan will catch most if not all help guides available, but take around 2-ish hours. Shallow scan takes only 5-10 minutes, but will only catch articles that are catagorized appropriately. The arguments are deep and shallow, the default is shallow.

Example Usage: python helpguide_crawler.py --scan deep

### Output:
This changes the output file to a location and file name, the arguments would look like "C:\path\you\would\ [like.txt]"

Example Usage: python helpguide_crawler.py --output "C:\path\you\would\[like.txt]"

## QA's:
Q: Why is slightly slow?   A: Initially I really wanted to thread this, but when I threaded these it most likely appeared the the TD domain as a DDOS type attack. In order to look over these html files and get the appropriate information it needs to run at a normal speed without threading.

Q: The site changes drastically, would this still be useful?   A: As long as the domain names are similar example: "https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID=11745" you can simply change the range (if the range changes at all), and it should still work as normal.

Q: Why does it give me the error: "File "c:\Users\taylor7337\Documents\BYUI-Web-Crawler\helpguide_crawler.py", line 1, in <module>
import requests"    A:   This is because you need to install beautifulsoup4 and request, refer to my prerequisits section above.

Q: What would be the purpose of something like this?   A: My manager wanted the information scraped from these websites to make it easy for an AI to train on. While working on it we realized this has a few different applications such as seeing guides that shouldn't be in the place it is, the domain names having a pattern, etc.