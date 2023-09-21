'''
Testing out different BeautifulSoup methods of finding things on websites.
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

WEBSITE = "https://www.pricecharting.com"
URL = "https://www.pricecharting.com/console/nes?sort=name&genre-name=&exclude-variants=true&exclude-hardware=true&when=none&release-date=2023-09-21&show-images=true"

request = requests.get(URL)
soup = BeautifulSoup(request.text, "html.parser")


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

first_url = games_list[0]["url"]
print(first_url)

game_data = []


response = requests.get(first_url)
response.raise_for_status()
first_game_soup = BeautifulSoup(response.text, "html.parser")
# game_info = soup.select(
#     "#game-page #full_details #attribute td.details")

game_data.append({
    "Title": games_list[0]["title"],
    "Release_Date": first_game_soup.find("td", itemprop="datePublished").getText(strip=True),
    "ESRB": first_game_soup.find("td", itemprop="contentRating").getText(strip=True),
    "Publisher": first_game_soup.find("td", itemprop="publisher").getText(strip=True),
    "Developer": first_game_soup.find("td", itemprop="author").getText(strip=True),
    "Genre": first_game_soup.find("td", itemprop="genre").getText(strip=True),
    "UPC": first_game_soup.find("td", itemprop="value").getText(strip=True),
    "URL": games_list[0]["url"],
    # "PriceCharting_ID": first_game_soup.find("td", itemprop="").getText(strip=True),
})
print(game_data)

df = pd.DataFrame(game_data)
print(df)

# for row in games_list:
#     print(row)

# print(games_list)
# print(first_game_title)
# print(first_game_url)
# print(soup.prettify())
