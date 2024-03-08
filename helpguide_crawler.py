import requests
import csv
from bs4 import BeautifulSoup
import os
import argparse
from deep_scan import main as deep_main
from shallow_scan import main as shallow_main

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='WebCrawler for HelpGuides at BYUI', add_help=False)

# Add arguments to the parser with modified default values
parser.add_argument('--scan', type=str, default='shallow', help='Specify if you would like to use the deep scan or shallow scan. Default is deep.')
parser.add_argument('--output', type=str, default='help_guide.csv', help='Change the output file to something different. Default is custom_output.csv.')
parser.add_argument('--rerun', type=bool, default=True, help='Rerun the list of URLs. Default is True.')

# Help message
parser.add_argument('--help', action='store_true', help='Show this help message')

# Parse the arguments
args = parser.parse_args()

# Check if the user requested help
if args.help:
    print("helpguide_crawler usage:")
    print("Use --help to bring this guide up again.")
    print("help arguments: none")
    print("Use --scan to specify if you would like to use the deep scan or shallow scan.")
    print("scan arguments: shallow, deep     Shallow is used by defualt")
    print("Use --rerun to rerun the list of urls (you might want to use this if it updated recently especially)")
    print("rerun arguments: true, false       False is used by default")
    print("Use --output to change the output file to something different.")
    print("output arguments: /path/you/would/like/[name of desired file].csv     help_guide.csv is used by default")

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e}")
        return None

def extract_header(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('h1').get_text().strip()

def extract_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = []
    tag_area = soup.select_one("#ctl00_ctl00_cpContent_cpContent_divTags")
    if tag_area is not None:
        for element in tag_area.descendants:
            if element.name == 'a':
                tags.append(element.get_text())
        massive_text = " ".join(tags)
        return massive_text
    else:
        return None


def extract_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs_and_headers = []
    par_area = soup.select_one("#ctl00_ctl00_cpContent_cpContent_divBody")
    if par_area is not None:
        for element in par_area.descendants:
            text = element.get_text()
            if ((element.name == 'p' or element.name == 'h2' or element.name == 'h3' or element.name == 'h4') and "Contact Us" not in text and 
                "Hours of Operation" not in text and "excluding weekly devotional" not in text and "this link" not in text):
                # This will exclude everything except p and h2 which are text and sub headings in these tags it will
                # exclude our hours of operation, contact info to prevent redundency, and
                # link so it doesn't promise a link that it won't deliver
                paragraphs_and_headers.append(text)
            
        massive_text = "    ".join(paragraphs_and_headers)
        massive_text = massive_text.replace("Â", " ") # removes the special character Â from text.
        return massive_text
    else:
        return None


def get_urls(txtFile):
    # Initialize an empty list to store the URLs
    urls = []
    with open(txtFile, 'r') as file:
    # Read each line in the file
        for line in file:
        # Remove any leading or trailing whitespace
            url = line.strip()
        # Add the URL to the list
            urls.append(url)
    return urls
# Display the list of URLs


def extract_info(url):
   
    html = get_page(url) 
    header = extract_header(html).strip()
    tags = extract_tags(html)
    paragraphs = extract_paragraphs(html)
    return header, tags, paragraphs


def export_csv(urls):
    with open('help_guide.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Header", "Tags", "Paragraphs"])
        for url in urls:
            print(url)
            header, tags, paragraphs = extract_info(url)
            writer.writerow([url, header, tags, paragraphs])

def main():
    
    text_file = 'article_urls.txt'
    if(args.rerun):
        if(args.scan == "deep"):
            deep_main()
            text_file = 'working_urls.txt'
        elif (args.scan == "shallow"):
            shallow_main()
        else:
            print("Sorry, I didn't understand your scanning preference")
            print("Using default")
            shallow_main()
    else: 
        print("skipping scan, exporting information to csv...")
    

    urls = get_urls(text_file)
    export_csv(urls)

if __name__ == '__main__':
    main()
    
