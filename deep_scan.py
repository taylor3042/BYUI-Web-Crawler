from bs4 import BeautifulSoup
import requests
# Deep scan takes about 2-3 hours to complete a full scan of articles in between
# help guides. If it gets out of bounds into KB's for employees it will shut down.

def get_page(url):
    try:
        response = requests.get(url)

        # making sure it's a valid url, before checking anything else
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def set_queue(working_urls):

    #change the range if this expands in the future.
    rstart = input("Select the starting range(or hit enter for default): ")
    rend = input("Select the ending range(or hit enter for default): ")
    if rstart or rend is None:
        print("None was selected for either number, using defaults")
        rstart = 10750
        rend = 14750
    
    for number in range(rstart, rend):
        # In the range (currently 10750-14740) check each number as a valid URL
        url = f'https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID={number}'
        check_url(url, working_urls)


def check_url(url, working_urls):
    response = get_page(url)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        body_tag = soup.find('body')

        # checks to see if the page is used for authenticating or as a public page
        if body_tag and 'cas' in body_tag.get('id', '') and 'login' in body_tag.get('class', ''):
            return None
        else:
            # enumeration helps the user know it's still running, might change this to an option later.
            print(url)
            working_urls.append(url)
    else:
        pass

def main():
    print("Using deep scan....")
    working_urls = []

    # shallow scan caught this, since it's way out of range I'm appending this at the beginning
    # change if this url name changes.
    working_urls.append('https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID=6306')
    set_queue(working_urls)
    with open('deep_scan.txt', 'a') as f:
        # this will write to deep_scan.txt for all the items in working_urls
        for urls in working_urls:
            f.write(f"{urls}\n")
        f.close()

if __name__ == '__main__':
    main()
