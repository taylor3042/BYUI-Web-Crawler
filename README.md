# BYUI-Web-Crawler

Author: Taylor Peterson

Purpose: Detecting and exporting info from BYUI help guides 

## Prerequisites

In order to run this software, you will need to have pthon 10 or greater installed. Using python's installer pip, you will need to install beautiful soup by using the command: pip install beautifulsoup4.

Depending on your Operating System (Windows, Linux, Apple), you will need to run this with python in your terminal. If you have Visual Studio Code editor (or another similar code editor) you can click the play button instead.

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

Example Usage: python helpguide_crawler.py --output "C:\path\you\would\ [like.txt]"