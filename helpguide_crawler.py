import requests
import csv
from bs4 import BeautifulSoup
import os
import argparse
import deep_scan
import shallow_scan


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process some integers.', add_help=False)

# Add arguments to the parser
parser.add_argument('--scan', type=str, default='shallow')
parser.add_argument('--output', type=str, default='help_guide.csv')
parser.add_argument('--rerun', type=bool, default= False)

# Add a custom help message
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
else:
    # Access the arguments
    print("Defualt Arguments Running")

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
    for element in tag_area.descendants:
        if element.name == 'a':
            tags.append(element.get_text())
    massive_text = " ".join(tags)
    return massive_text


def extract_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        # Check if the paragraph contains any 'a' tags (hyperlinks)
        if (not p.find('a') and "Contact Us" not in p.get_text() and "Hours of Operation" not in p.get_text()):
            # If no 'a' tags found, Contact Us is not in text, and Hours of Operation, add the text to the result
            # Both text checks make sure that they don't get redundant information
            paragraphs.append(p.get_text())
    
    massive_text = "\n".join(paragraphs)
    return massive_text

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
    header = extract_header(html)
    tags = extract_tags(html)
    paragraphs = extract_paragraphs(html)
    print(header)
    print(url)
    print(tags)
    print(paragraphs)
    return header, tags, paragraphs


def export_csv(urls):
    with open('help_guide.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Header", "Tags", "Paragraphs"])
        for url in urls:
            header, tags, paragraphs = extract_info(url)
            writer.writerow([url, header, tags, paragraphs])  # 


def main():
    urls = get_urls('article_urls.txt')
    export_csv(urls)

if __name__ == '__main__':
    main()
    
