import os

import requests

creator_list = [
    116282456784,  # Allegro.cz  ,CZ
    # 70488720814,        #Alza.cz  ,CZ
    # 1731653497124334,   #Alza.hu  ,HU
    # 105084766225021,    #Alza.sk  ,SK
    # 108369512515592,    #Andreashop.sk  ,SK
    # 113323268702404,    #COMFOR  ,CZ
    # 244816482042,       #czc.cz  ,CZ
    # 133129068446,       #DATART CZ  ,CZ
    # 113999741958452,    #Datart SK  ,SK
    # 311023942288608,    #Electro World  ,CZ
    # 193077740858915,    #eMAG Magyarország  ,HU
    # 249422102855,       #Euronics HU  ,HU
    18349420804,  # Heureka.cz  ,CZ
    # 376687425389,       #Heureka.sk  ,SK
    # 376809572404232,    #Kaufland Česká republika  ,CZ
    252811101430384,  # Media Markt Magyarország  ,HU
    237743655098,  # Megapixel.cz  ,CZ
    159236480801841,  # Mobil Pohotovost  ,CZ
    265388683512099,  # NAY  ,SK
    # 127897760593066,    #Okay.cz  ,CZ
    # 194472407335619,    #Okay.sk  ,SK
    338869025332,  # ONLINESHOP.cz  ,CZ
    256989857726255,  # Planeo  ,CZ
    # 200012756732328,    #eberry.cz  ,CZ
    # 173362889874706,    #PLANEO Elektro SK  ,SK
    # 113198873242,       #Internet Mall Slovakia s.r.o.  ,SK
]

for creator_id in creator_list:
    # List of image IDs
    file_path = (
        f"meta_data_ids/meta_ids_{creator_id}.txt"
    )  # Replace with your file's path
    with open(file_path, "r", encoding="utf-8") as file:
        ids = file.read().split(",")

    # Folder where you want to save the downloaded images
    download_folder = f"downloaded_images/{creator_id}"

    # Create the download folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    for id in ids:
        # Construct the image URL using the ID
        image_url = f"https://facebook-ad-previews.nexxxt.cloud/{id}.jpg"

        # Extract the file name from the URL
        file_name = os.path.join(download_folder, f"{id}.jpg")

        # Send an HTTP GET request to the URL
        response = requests.get(image_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the file in binary write mode and write the image content to it
            with open(file_name, "wb") as f:
                f.write(response.content)
            print(f"Image downloaded as {file_name}")
        else:
            print(
                f"Failed to download the image from {image_url}. Status code: {response.status_code}"
            )
