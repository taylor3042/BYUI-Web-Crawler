import threading


def removeSIDs(file):
    with open(file, 'r') as f:
        urls = f.readlines()
    
    modified_urls = []
    for url in urls:
        url = url.strip()
        params = url.split('&')
        modified_url = url
        for param in params:
            if param.startswith('SIDs='):
                print("Removing SIDs:", param)
                modified_url = modified_url.replace(param, '')
                break
        if modified_url.endswith('&'):
            # Removes the trailing '&' as well
            modified_url = modified_url[:-1]  
        modified_urls.append(modified_url)

    with open(file, 'w') as f:
        f.writelines('\n'.join(modified_urls))


    
# Function to check for duplicates in a queue labeled 'chunks'
def check_duplicates(chunk, result):
    duplicates = set()
    seen = set()

    for url in chunk:
        url = url.strip()
        if url in seen:
            duplicates.add(url)
            print(f'Found duplicate: {url}')
        else:
            seen.add(url)

    result.update(seen)

# Function to split a list into chunks so the computer is not overwhellmed
def chunkify(lst, num_chunks):
    chunk_size = len(lst) // num_chunks
    chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunks

# Main function to find duplicates using threading
def find_duplicates_from_file(file_path, num_threads=4):
    result = set()
    threads = []

    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    chunks = chunkify(urls, num_threads)

    for chunk in chunks:
        thread = threading.Thread(target=check_duplicates, args=(chunk, result))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    
    with open(file_path, 'w') as f:
        f.writelines('\n'.join(result))


def main():
    file_path = 'article_urls.txt'
    print("Cleaning up URL file....")
    removeSIDs(file_path)
    find_duplicates_from_file(file_path)

if __name__ == '__main__':
    main()