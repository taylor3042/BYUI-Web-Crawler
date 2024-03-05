from bs4 import BeautifulSoup
import requests
# Deep scan takes about 2-3 hours to complete a full scan of articles in between
# help guides. If it gets out of bounds into KB's for employees it will shut down.

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def set_queue(working_urls):

    threads = []
    # change the range if this expands in the future.
    for number in range(10750, 14750):
        url = f'https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID={number}'
        #url = 'https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID=14024'
        check_url(url, working_urls)


def check_url(url, working_urls):
    response = get_page(url)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        body_tag = soup.find('body')
        if body_tag and 'cas' in body_tag.get('id', '') and 'login' in body_tag.get('class', ''):
            return None
        else:
            print(url)
            working_urls.append(url)
    else:
        pass

    # catch <body id="cas" class="login">

def main():
    print("Using deep scan....")
    working_urls = []
    set_queue(working_urls)
    with open('deep_scan.txt', 'a') as f:
        for urls in working_urls:
            f.write(f"{urls}\n")
        f.close()

if __name__ == '__main__':
    main()
