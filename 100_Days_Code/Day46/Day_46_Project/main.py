from bs4 import BeautifulSoup
from requests import HTTPError
import requests
import re

# URL of website to be scraped:
URL = "https://www.billboard.com/charts/hot-100/"

# Request the website and save the html content into a "soup"
while True:
    try:
        date_to_search = input(
            "Please enter a date to return the top 100 songs for that week. (YYYY-MM-DD): ")
        response = requests.get(URL + date_to_search)
        response.raise_for_status()
    except HTTPError:
        print(
            f"The text you entered, {date_to_search}, is in the incorrect format.\n")
        continue
    break

soup = BeautifulSoup(response.text, "html.parser")


### NOT WORKING ###
# titles_html = soup.find(name="h3", id="title-of-a-story",
# class_=re.compile("c-title[ ]{2}.*"))
### NOT WORKING ###


# Extract specific title and article html
titles_html = soup.select("body li h3", id="title-of-a-story")

# Create list for storing tuples of artist and song:
all_songs = []

# titles_html  has extra elements for some reason after the song names that I can't get rid of
# therefore just slicing it to the first 100 elements. Also getting artist info:
for title in titles_html[:100]:
    song_title = title.getText().strip()
    artist = title.find_parent().find('span').getText().strip()
    # print(f"{song_title}  --> Tag: {artist}")
    all_songs.append((artist, song_title))

# Debugging print for sanity check:
count = 1
for song in all_songs:
    print(f"{count}. {song}")
    count += 1


### OLD CODE FOR OLD SITE ###
# titles_html = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# artist_html = soup.find_all(
# name="span", class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")

# top_100_titles = [item.string for item in titles_html]
# top_100_artists = [item.string for item in artist_html]
# combined_top_100 = zip(top_100_titles, top_100_artists)

# combined_top_100 list is in this format: [('Shake Ya Tailfeather', 'Nelly, P. Diddy & Murphy Lee'),...]
# Print the top 100
# for count, song in enumerate(combined_top_100):
# print(f"{count+1}. '{song[0]}' by {song[1]}")
### OLD CODE FOR OLD SITE ###
