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
    json_file_path = 'sample.json'
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


    for item in data:
        for word in words_to_remove:
            item['content'] = item['content'].replace(word, '')
        item['content'] = item['content'].replace('\u00a0', '')
        item['content'] = item['content'].replace('**', '')
        item['topic'] = item['topic'].replace('\u00a0', '')
        item['topic'] = item['topic'].replace(' ', '')
        item['topic'] = item['topic'].replace('\"', '')
        item['content'] = item['content'].replace('\n', '')
        item['content'] = item['content'].replace('\"', '')
        item['content'] = item['content'].replace('\t', '')
        item['content'] = item['content'].replace('\u200b', '')
        item['content'] = item['content'].replace('\u201c', '')
        item['content'] = item['content'].replace('\u201d', '')
        item['content'] = item['content'].replace('\u2013', '')
        item['content'] = item['content'].replace('\u2003', '')
        item['content'] = item['content'].replace('\u2019', '')
        item['content'] = item['content'].replace('\u2026', '')
        item['content'] = item['content'].replace('\u202f', '')
        item['content'] = item['content'].replace('\u2014', '')


    for item in data:
        item['content'] = item['content'].replace(' ', '')
    data = data[1:]

    # Write the modified data back to the same JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    main()