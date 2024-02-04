import json
import os

import requests

# Define the API endpoint URL
output_dir = "meta_data_ids"  # Directory to save the JSON files

# List of IDs to use as parameters
id_list = [
    116282456784,  # Allegro.cz  ,CZ
    70488720814,  # Alza.cz  ,CZ
    1731653497124334,  # Alza.hu  ,HU
    105084766225021,  # Alza.sk  ,SK
    108369512515592,  # Andreashop.sk  ,SK
    113323268702404,  # COMFOR  ,CZ
    244816482042,  # czc.cz  ,CZ
    133129068446,  # DATART CZ  ,CZ
    113999741958452,  # Datart SK  ,SK
    311023942288608,  # Electro World  ,CZ
    193077740858915,  # eMAG Magyarország  ,HU
    249422102855,  # Euronics HU  ,HU
    18349420804,  # Heureka.cz  ,CZ
    376687425389,  # Heureka.sk  ,SK
    376809572404232,  # Kaufland Česká republika  ,CZ
    252811101430384,  # Media Markt Magyarország  ,HU
    237743655098,  # Megapixel.cz  ,CZ
    159236480801841,  # Mobil Pohotovost  ,CZ
    265388683512099,  # NAY  ,SK
    127897760593066,  # Okay.cz  ,CZ
    194472407335619,  # Okay.sk  ,SK
    338869025332,  # ONLINESHOP.cz  ,CZ
    256989857726255,  # Planeo  ,CZ
    200012756732328,  # eberry.cz  ,CZ
    173362889874706,  # PLANEO Elektro SK  ,SK
    113198873242,  # Internet Mall Slovakia s.r.o.  ,SK
]

# Create the output directory if it doesn't exist

os.makedirs(output_dir, exist_ok=True)
# Create the output directory if it doesn't exist
access_token = "EAALnc8im5MUBO6ZBSzHKyLGKN5xnAVNEZBGsS6zuAQjRPUQYvyIZCqDWGshJs0xUDyEeNYnojFcwgZAU2nJEU1EsYYOt7U6hwqDZCfoZCAdzPuK5yXAYZAy0dBM91OjyTNaKa8jazZAjwZBYSIbCoexzAwVJmbKC78jTCOtu8TvvqpxbCUH0j106QZAZAw9WR6bx8nisaG593oNQuzKzeY35gxGjvyZBKcyaY3FZBkQZDZD"

# Loop through the list of IDs
for id in id_list:
    fields = "id"
    supported_countries = [
        "AT",
        "BE",
        "BG",
        "CA",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GB",
        "GR",
        "HR",
        "HU",
        "IE",
        "IL",
        "IN",
        "IT",
        "LT",
        "LU",
        "LV",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SE",
        "SI",
        "SK",
        "UA",
        "US",
    ]
    api_url = f"https://graph.facebook.com/v17.0/ads_archive?search_terms=&ad_type=ALL&ad_reached_countries={supported_countries}&access_token={access_token}&unmask_removed_content=true&search_page_ids={id}&fields={fields}&limit=999]"

    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data from the response
        api_data = response.json()

        # Extract the "data" key from the API response
        data = api_data.get("data")

        if data:
            # Save the "data" list as a JSON file with a filename based on the ID
            filename = os.path.join(output_dir, f"meta_ids_{id}.json")
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)

            # Extract and save the values from the dictionaries as a comma-separated string
            values = [item.get("id") for item in data if isinstance(item, dict)]
            comma_separated_values = ",".join(values)

            # Save the comma-separated values in a text file with a filename based on the ID
            filename = os.path.join(output_dir, f"meta_ids_{id}.txt")
            with open(filename, "w", encoding="utf-8") as txt_file:
                txt_file.write(comma_separated_values)

            print(f"Data for ID {id} saved as {filename}")
        else:
            print(f"No 'data' key found in the API response for ID {id}")
    else:
        print(
            f"API request for ID {id} failed with status code: {response.status_code}"
        )
