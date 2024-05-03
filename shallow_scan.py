import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

base_url = "https://td.byui.edu/"

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e} The URL is: {url}")
        return None

def find_cat(html, urls):
    soup = BeautifulSoup(html, 'html.parser')
    div_cats = soup.select_one("#divCats")
    
    for element in div_cats.descendants:
        if element.name == 'a':
            path = element.get_text()
            if(exceptions(path)):
                full_url = urljoin(base_url, element.get('href'))
                urls.append(full_url)
                #print(full_url, element.get_text())


def find_art(cat_urls, art_urls):
    for url in cat_urls:
        if "CategoryID" in url:
            find_cat(get_page(url), cat_urls)  # Recursion to loop back until there's no more categories.
        elif "ArticleDet" in url:
            #print(f'Url is: {url} and length is {len(url)}')
            art_urls.append(url)
        else:
            print("ERROR!")


def exceptions(links):
    exception = str(links).strip()
    if(exception != "Expand" and exception is not None):
        #I'm leaving this open to find more exception to have under the tag I found that work for catagories.
        return True
    else:
        return False


def main():
    print("Using shallow scan...")
    cat_urls = [] #catagory pages
    art_urls = [] #article pages
    # starting_path = 'https://td.byui.edu/TDClient/79/ITHelpCenter/KB/?CategoryID=1875'
    starting_path = 'https://td.byui.edu/SBTDClient/79/ITHelpCenter/KB/?CategoryID=1566'
    find_cat(get_page(starting_path), cat_urls)
    find_art(cat_urls, art_urls)
    
    with open('article_urls.txt', 'w') as f:
        for urls in art_urls:
            f.write(f"{urls}\n")

if __name__ == '__main__':
    main()