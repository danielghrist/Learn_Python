'''
Testing out different BeautifulSoup methods of finding things on websites.
'''

import requests
import pandas as pd
# import time
from scraper_helper import Scraper
from bs4 import BeautifulSoup
from pathlib import Path


# Create a path to where we are running this script from to find data files:
REL_FILE_PATH = Path(__file__, "../").resolve()
CONSOLE = "nes"
WEBSITE = "https://www.pricecharting.com"
URL = f"https://www.pricecharting.com/console/{CONSOLE}?sort=name&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2023-09-21&show-images=true"

# Create Scraper object for CONSOLE to scroll to bottom of the page.
console_scrape = Scraper(CONSOLE)
console_scrape.scroll_to_bottom()
html = console_scrape.get_page_source()
console_scrape.close_webdriver()

# Request the source of the webpage pointed to by URL:
# request = requests.get(URL)
# request.raise_for_status()
soup = BeautifulSoup(html, "html.parser")


### ----- TESTING WITH JUST FINDING ONE ELEMENT USING CSS SELECTORS ----- ###
# first_game_url = soup.select_one(
#     "#games_table tbody tr td.title a").get("href")
# first_game_title = soup.select_one(
#     "#games_table tbody tr td.title").getText().replace("\n", "")
### ----- END TESTING WITH JUST FINDING ONE ELEMENT USING CSS SELECTORS ----- ###

# Get a list of all the td's in the game table with a class of "title":
game_rows = soup.select(
    "#games_table tbody tr td.title")

# List to hold dictionaries of the title and url of each game
games_list = []

# Loop through all the td's with class "title" that were found and add the title and url as dict to # games_list
for rows in game_rows:
    title = rows.getText().replace("\n", "")
    url = f"{WEBSITE}{rows.find(name='a').get('href')}"
    games_list.append({
        "title": title,
        "url": url
    })

print(len(games_list))

game_data = []
print("Scraping data...")
for i in range(0, len(games_list)):
    print(f"Scraping for game #: {i:04}: {games_list[i]['title']}")
    session_object = requests.Session()
    response = session_object.get(games_list[i]["url"])
    # response.raise_for_status()
    game_soup = BeautifulSoup(response.text, "html.parser")

    game_data.append({
        "Title": games_list[i]["title"],
        "Release_Date": game_soup.find("td", itemprop="datePublished").getText(strip=True),
        "ESRB": game_soup.find("td", itemprop="contentRating").getText(strip=True),
        "Publisher": game_soup.find("td", itemprop="publisher").getText(strip=True),
        "Developer": game_soup.find("td", itemprop="author").getText(strip=True),
        "Genre": game_soup.find("td", itemprop="genre").getText(strip=True),
        "UPC": game_soup.find("td", itemprop="value").getText(strip=True),
        "PriceCharting_ID": game_soup.find("td", class_="title", string="PriceCharting ID:").findNextSibling().getText(strip=True),
        "Description": game_soup.find("td", itemprop="description").getText(strip=True),
        "URL": games_list[i]["url"],
    })
    # time.sleep(2)

# Create DataFrame to save data to CSV:
df = pd.DataFrame(game_data)
# Add column in DataFrame for the current CONSOLE:
df.insert(0, "Platform", CONSOLE)
print(df.head())

# Save df with all game data to a csv file:
df.to_csv(REL_FILE_PATH.joinpath(
    f"{console_scrape.get_string_date()}-{console_scrape.get_console()}-Game_List.csv"))

print("Finished Scraping and saving to csv file.")
