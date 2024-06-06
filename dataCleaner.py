import csv
import json

def main():
    print("Extracting and cleaning from csv to json......")
    # Define the indices of the columns to extract
    url_index = 0
    topic_index = 1
    content_index = 3
    csv_file = 'help_guide.csv'
    words_to_remove = ["Issue", "Environment", "resolution", "Escalation", "Cause", "Resolution", "Tier 1","for", "TIER 1", "the", "a", "and", "an", "The"]
    # Initialize an empty list to store the extracted data
    data = []
    json_file_path = 'help_guide.json'
    # Read the CSV file and extract the specified columns
    with open(csv_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) > max(url_index, topic_index, content_index):
                url = row[url_index]
                topic = row[topic_index]
                content = row[content_index]
                data.append({'url': url, 'topic': topic, 'content': content})

    # Write the extracted data to a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


    # Read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # This seems too long to work efficently, and it's in part due to
    # the actual data it retrieves. The escape character can't be removed
    # by simply converting it back from csv to json again. So the simplist
    # and best working solution was to use the replace function to remove
    # specific escape characters. This whole program averages 0.8 seconds
    # so the size of this section doesn't seem to have a large effect.
    for item in data:
        for word in words_to_remove:
            item['content'] = item['content'].replace(word, '')
        item['content'] = item['content'].replace('\u00a0', '')
        item['content'] = item['content'].replace('**', '')
        item['topic'] = item['topic'].replace('\u00a0', '')
        item['topic'] = item['topic'].replace(' ', '')
        item['topic'] = item['topic'].replace('\"', '')
        item['topic'] = item['topic'].replace('\u2019', '')
        item['content'] = item['content'].replace('\n', '')
        item['content'] = item['content'].replace('\"', '')
        item['content'] = item['content'].replace('\t', '')
        item['content'] = item['content'].replace('\udc17', '')
        item['content'] = item['content'].replace('\ud83e', '')
        item['content'] = item['content'].replace('\u2019', '')
        item['content'] = item['content'].replace('\u2b07', '')
        item['content'] = item['content'].replace('\ufe0f', '')
        item['content'] = item['content'].replace('\u200b', '')
        item['content'] = item['content'].replace('\u201c', '')
        item['content'] = item['content'].replace('\u201d', '')
        item['content'] = item['content'].replace('\u2013', '')
        item['content'] = item['content'].replace('\u2003', '')
        item['content'] = item['content'].replace('\u2026', '')
        item['content'] = item['content'].replace('\u202f', '')
        item['content'] = item['content'].replace('\u2014', '')

    # Removes any more spaces (there should only be a few more)
    for item in data:
        item['content'] = item['content'].replace(' ', '')
        item['content'] = item['content'].replace('\udc17', '')
        item['content'] = item['content'].replace('\ud83e', '')
    data = data[2:]
    # Writes the modified data back to the same JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    main()
