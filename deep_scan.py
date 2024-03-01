import requests
# Deep scan takes about 2-3 hours to complete a full scan of articles in between
# help guides. If it gets out of bounds into KB's for employees it will shut down.

def get_page(url, working_urls):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            working_urls.append(url)
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e}")
        return None

def set_queue(working_urls):

    threads = []
    # change the range if this expands in the future.
    for number in range(10750, 14750):
        url = f'https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID={number}'
        get_page(url, working_urls)


def main():
    working_urls = []
    set_queue(working_urls)

    with open('working_urls.txt', 'a') as f:
        for urls in working_urls:
            f.write(f"{urls}\n")
            #print(urls)
        f.close()

if __name__ == '__main__':
    main()
