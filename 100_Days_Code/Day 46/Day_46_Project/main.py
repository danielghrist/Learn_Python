from bs4 import BeautifulSoup
from requests import HTTPError
import requests


URL = "https://www.billboard.com/charts/hot-100/"

# Request the website and save the html content into a "soup"
while True:
    try:
        date_to_search = input("Please enter a date to return the top 100 songs for that week. (YYYY-MM-DD): ")
        response = requests.get(URL + date_to_search)
        response.raise_for_status()
    except HTTPError:
        print(f"The text you entered, {date_to_search}, is in the incorrect format.\n")
        continue
    break

soup = BeautifulSoup(response.text, "html.parser")

# Extract specific title and article html
titles_html = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artist_html = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

top_100_titles = [item.string for item in titles_html]
top_100_artists = [item.string for item in artist_html]
combined_top_100 = zip(top_100_titles, top_100_artists)

# combined_top_100 list is in this format: [('Shake Ya Tailfeather', 'Nelly, P. Diddy & Murphy Lee'),...]
# Print the top 100
for count, song in enumerate(combined_top_100):
    print(f"{count+1}. '{song[0]}' by {song[1]}")


