from bs4 import BeautifulSoup
import requests
import json


# with open("website.html", encoding="utf-8") as file:
# website_html = file.read()

# soup = BeautifulSoup(website_html, "html.parser")

# # print(soup.findAll(name="p"))
#
# # for tag in soup.findAll(name="a"):
# #     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(selector=".heading")
# print(headings)


# response = requests.get("https://news.ycombinator.com/")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
#
# story_links = soup.find_all(class_="storylink")
# upvotes = soup.find_all(class_="score")
#
# # Taking data that was scraped with Beautiful Soup from news.ycombinator.com and creating a dictionary
# new_dict = []
# for link in story_links:
#     if "ycombinator.com" not in link.get("href"):  # skipping over ycombinator link because it does not include upvotes
#         new_dict.append({"link": link.get("href"), "title": link.string})
#
# for count, upvote in enumerate(upvotes):
#     print(f"count: {count}")
#     print(f"upvote: {upvote}")
#     print(f"items: {new_dict[count]}")
#     new_dict[count].update({"upvotes": int(upvote.string.split(" ")[0])})
#
#
# max_upvotes = (max(item["upvotes"] for item in new_dict))

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Request the website and store the html into the empire_top_100_movies variable:
response = requests.get(URL)
empire_top_100_movies = response.text

#### WEBSITE CHANGED NOW USES H3 WITH CLASS=listicleItem_listicle-item__title__hW_Kn FOR TITLE ####
soup = BeautifulSoup(empire_top_100_movies, "html.parser")

# Get the name of the movies in a list while getting rid of the <number)> and strip whitespace:
tags = soup.findAll(
    name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_names = [name.getText().split(")")[1].strip() for name in tags]

# Reverse the list of movie names as the website starts at the end:
movie_names.reverse()

# Loop through the movie names and at a number for each one and print title:
for i, name in enumerate(movie_names, start=1):
    print(f"{i:02}. {name}")


### OLD CODE ###
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Request the website and store the html into the empire_top_100_movies variable:
# response = requests.get(URL)
# empire_top_100_movies = response.text

# Scrape website and pull the h3 tags with class=jsx-4245974604 which are the titles of the movies:
# soup = BeautifulSoup(empire_top_100_movies, "html.parser")
# website_json = json.loads(soup.find("script", type="application/json").text) # ???


# Movie titles found in this dictionary and key:
# movies["props"]["pageProps"]["apolloState"]["ImageMeta:5e6224d408baaa5a8143279c"]["titleText"]
# top_100_movies = []
# for item in website_json["props"]["pageProps"]["apolloState"]:
#     if website_json["props"]["pageProps"]["apolloState"][item].get("titleText") is not None:
#         top_100_movies.append(
#             website_json["props"]["pageProps"]["apolloState"][item].get("titleText"))

# print(top_100_movies)

# Save
# with open("movies.txt", "w", encoding="utf8") as file:
#     # for i in range(len(top_100_movies), 0, -1):
#     file.writelines([f"{top_100_movies[i]}\n" for i in range(
#         len(top_100_movies) - 1, -1, -1)])
### OLD CODE ###
