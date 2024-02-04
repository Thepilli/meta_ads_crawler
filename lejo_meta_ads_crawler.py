import json
import re

import requests

# List of reference numbers
reference_numbers = []

# Define the regex pattern
pattern = r'\\ud.{3}\\ud.{3}'

# Initialize an empty list to store JSON data
json_data_list = []

# Loop through the reference numbers
for ref_number in reference_numbers:
    url = f"https://ad-archive.nexxxt.cloud/ad/{ref_number}"

    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        json_data = response.json()

        # Convert the JSON data to a JSON string
        json_string = json.dumps(json_data)

        # Use regex to replace the specified pattern with empty spaces
        json_string = re.sub(pattern, '', json_string)

        # Append the modified JSON data back to a dictionary
        modified_json_data = json.loads(json_string)
        json_data_list.append(modified_json_data)
    else:
        print(f"Failed to fetch data for reference number {ref_number}")

# Write all the JSON data to a single file with UTF-8 encoding
with open('meta_ad_library_alza.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_data_list, outfile, indent=4, ensure_ascii=False)

print("Data fetched and saved to 'meta_ad_library_alza.json'")