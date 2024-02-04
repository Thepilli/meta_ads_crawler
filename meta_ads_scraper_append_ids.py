import json
import os

folder_path = "C:/Users/jiri.pillar/Developer/python/meta_ads_crawler/meta_data_ids"
combined_data = []
json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]



for file_name in json_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r",encoding="utf-8") as file:
        data = json.load(file)
        combined_data.extend(data)
final_data = combined_data


output_file = os.path.join(folder_path,"meta_ads_combined_data.json")
with open(output_file, "w",encoding='utf-8') as output:
    json.dump(final_data, output, indent=4, ensure_ascii=False)

print(f"Combined data saved to {output_file}")