import csv
import re
import json

def remove_words_from_csv(input_file, output_file, words_to_remove):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                # Remove words/statements from the third column (index 2)
                row[3] = remove_words(row[3], words_to_remove)
                writer.writerow(row)

def remove_words(text, words_to_remove):
    for word in words_to_remove:
        text = re.sub(r'\b' + re.escape(word) + r'\b', '', text, flags=re.IGNORECASE)
    return text.strip()

def remove_spaces_from_csv(file_path):
    # Read the content of the file into memory
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Remove spaces from each element in each row
    for row_index, row in enumerate(rows):
        rows[row_index] = [element.replace(" ", "") for element in row]
    rows[3] = [element.replace(" ", "") for element in row]

    # Write the modified content back to the same file
    with open(file_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

# Example usage:
input_file = "hgcopy.csv"
output_file = "hgsample.csv"
words_to_remove = ["Issue", "Environment", "Resolution for TIER 1", "Escalation", "Cause", "resolution", "for", "TIER 1"]

remove_words_from_csv(input_file, output_file, words_to_remove)

for _ in range(2):
    remove_spaces_from_csv(output_file)

# Define the indices of the columns to extract
url_index = 0
topic_index = 1
content_index = 3

# Initialize an empty list to store the extracted data
data = []
json_file_path = 'sample.json'
# Read the CSV file and extract the specified columns
with open(output_file, 'r', encoding='utf-8-sig') as csv_file:
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

# Remove "\u00a0" from the content
for item in data:
    item['content'] = item['content'].replace('\u00a0', '')
    item['content'] = item['content'].replace('\u00a0', '')

data = data[1:]

# Write the modified data back to the same JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)