# This program can run and check the differences between deep_scan and shallow_scan.txt 
# With knowing the differences and similarities it should help fix probelms with the code.

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


def main():
    # change the names of the txt files as needed
    su = get_urls('shallow_scan.txt')
    du = get_urls('deep_scan.txt')
    sameList = []
    differentList = []
    for shallow_url in su:
        found_match = False
        url_string = shallow_url
        for deep_url in du:
            if (str(deep_url) == str(url_string)):
                sameList.append(url_string)
                print(f'found shallow same url: {shallow_url}')
                print(f'found deep same url: {url_string}')
                found_match = True
            else:
                pass
        if not found_match:
            print(f'found a different url :( {shallow_url}')
            differentList.append(shallow_url)
    
    with open('same_URLS.txt', 'a') as f:
        for urls in sameList:
            f.write(f"{urls}\n")
        f.close()
    with open('different_URLS.txt', 'a') as f:
        for urls in differentList:
            f.write(f"{urls}\n")
        f.close()
    print("finished process, closing the program.")


if __name__ == '__main__':
    main()