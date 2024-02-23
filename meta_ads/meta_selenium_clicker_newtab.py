import time

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

creator_list=[

## 116282456784,       #Allegro.cz  ,CZ
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
## 18349420804,        #Heureka.cz  ,CZ
# 376687425389,       #Heureka.sk  ,SK
# 376809572404232,    #Kaufland Česká republika  ,CZ
# 252811101430384,    #Media Markt Magyarország  ,HU
# 237743655098,       #Megapixel.cz  ,CZ
# 159236480801841,    #Mobil Pohotovost  ,CZ
# 265388683512099,    #NAY  ,SK
# 127897760593066,    #Okay.cz  ,CZ
# 194472407335619,    #Okay.sk  ,SK
# 338869025332,       #ONLINESHOP.cz  ,CZ
# 256989857726255,    #Planeo  ,CZ
# 200012756732328,    #eberry.cz  ,CZ
# 173362889874706,    #PLANEO Elektro SK  ,SK
## 113198873242,       #Internet Mall Slovakia s.r.o.  ,SK

]

for creator_id in creator_list:

    # List of image IDs
    file_path = f"meta_data_ids/meta_ids_{creator_id}.txt"  # Replace with your file's path
    with open(file_path, "r", encoding="utf-8") as file:
        ids = file.read().split(',')



    # Initialize the WebDriver (you might need to specify the path to your WebDriver executable)
    driver = webdriver.Chrome()


    for id in ids:
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.set_window_size(1080, 1920)

        url = f'https://ad-archive.nexxxt.cloud/#{id}'

        driver.get(url)

        try:
            # Wait for the "Toggle preview" button to become clickable (up to 10 seconds)
            wait = WebDriverWait(driver, 10)
            toggle_preview_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div[2]/div[3]/a"))
            )

            try:
                # Click the button
                toggle_preview_button.click()
                time.sleep(3)  # Add a 3-second delay
            except ElementClickInterceptedException:
                print("ElementClickInterceptedException: Skipping and continuing the loop.",url)
                continue
            # Close the current tab
            driver.close()

            # Switch to the main tab
            driver.switch_to.window(driver.window_handles[0])

        except TimeoutException:
            print("Timeout waiting for 'Toggle preview' button to become clickable on", url)

    # Close the main tab when done
    # driver.quit()

