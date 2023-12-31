'''
Program to scrape game price data for loose, CIB, and new versions of the game and save to csv for that date. The console that is being scraped can be changed by changing the CONSOLE constant.
'''
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver import Keys
from datetime import datetime
from pathlib import Path


# Create a path to where we are running this script from to find data files:
REL_FILE_PATH = Path(__file__, "../").resolve()

### -----BEGIN CONSTANTS----- ###
# Constant to use for which console we want to search for:
CONSOLE = "wii"
# Amount to pause between each scroll action:
SCROLL_PAUSE_TIME = .5
# URL with filtered search for Wii game on price charting site:
URL = f"https://www.pricecharting.com/console/{CONSOLE}?sort=name&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2023-09-07&show-images=true"
### -----END CONSTANTS----- ###


# Get current date as a string in YYYY_MM_DD format:
def getStringDate() -> str:
    '''Returns the current date in YYYY_MM_DD format.'''
    return datetime.today().strftime("%Y_%m_%d")


# Get Chrome options and set up brower to not auto close:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create webdriver:
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

# Code to scroll to bottom of page using execute to execute JavaScript code:
# Get current scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to bottom of current visible window:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the page to load:
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
### End scrolling to bottom of page ###

game_price_list = []

# Obtain all row data in the #games_table on the website:
game_data_row = driver.find_elements(
    By.CSS_SELECTOR, "#games_table tbody tr")
# print(game_data_row)


# Loop through each row and extract image, title, loose price, cib_price, and new_price
i = 0
for row in game_data_row:
    print(f"Scraping row #{i:04}.")
    price_charting_id = row.get_attribute("data-product")
    # Find the URL of the thumbnail view of a game image:
    image_src = row.find_element(
        By.CSS_SELECTOR, "td div img.photo").get_property("src")
    title = row.find_element(By.CSS_SELECTOR, "td.title").text
    loose_price = row.find_element(
        By.CSS_SELECTOR, "td.used_price").text.replace("$", "")
    cib_price = row.find_element(
        By.CSS_SELECTOR, "td.cib_price").text.replace("$", "")
    new_price = row.find_element(
        By.CSS_SELECTOR, "td.new_price").text.replace("$", "")
    ### DEBUG PRINT ###
    # print(
    # f"Title: {title} | Loose Price: {loose_price} | CIB Price: {cib_price} | New Price: {new_price}")
    ### DEBUG PRINT ###
    # Add data for each game to game_dict dictionary:
    game_price_list.append({
        "PC_ID": price_charting_id,
        "title": title,
        "loose_price": loose_price,
        "cib_price": cib_price,
        "new_price": new_price,
        "image_link": image_src,
    })
    i += 1


# Close the webdriver browser:
driver.quit()

game_df = pd.DataFrame(game_price_list)
print(game_df)
game_df.to_csv(REL_FILE_PATH.joinpath(
    f"{getStringDate()}-{CONSOLE.title()}-Price_List.csv"))


# print(game_dict)
# print()
# pprint.pprint(game_dict)

# element = driver.find_element(By.CSS_SELECTOR, "body")

### WAS TRYING OUT USING ACTIONCHAIN TO HOLD END KEY TO SCROLL TO BOTTOM OF PAGE BUT DIDN'T WORK ###
# Create ActionChain to scroll to the bottom to make all games visible:
# action_chain = ActionChains(driver)
# action_chains.scroll(x: int, y: int, delta_x: int, delta_y: int, duration: int = 0, origin: str = 'viewport').perform()
# action_chain.send_keys_to_element(element, Keys.END)
# action_chain.key_down(Keys.END, element)
# action_chain.perform()
### WAS TRYING OUT USING ACTIONCHAIN TO HOLD END KEY TO SCROLL TO BOTTOM OF PAGE BUT DIDN'T WORK ###
