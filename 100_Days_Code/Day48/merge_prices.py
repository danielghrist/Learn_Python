'''
Script to merge my personal collection with the price data I have scraped to get up to date pricing info so I know what is worth selling and what isn't.
'''
import re
import pandas as pd
# import difflib
from pathlib import Path

# Console to get prices for:
CONSOLE = "Wii"

# Create a path to where we are running this script from to find data files:
REL_FILE_PATH = Path(__file__, "../").resolve()

# Load personal collection data as Pandas DataFrame:
collection = pd.read_csv(REL_FILE_PATH.joinpath(
    "iCollect Everything All-2022_01_13.csv"))

# Load pricing data as Pandas Dataframe:
pricing = pd.read_csv(REL_FILE_PATH.joinpath("2023-09-10-Wii-Price_List.csv"))

# Create DataFrame with only includes the CONSOLE I want to view prices for:
console_collection = collection.query(f"Platform == '{CONSOLE}'").reset_index()

# Rename the Title column header in the collection data to match the pricing data:
console_collection.rename(columns={"Title": "title"}, inplace=True)

### ----- BOTH OF THESE METHODS WORK BUT REMOVE SPACES AS WELL----- ###
# Try to use str.replace with regex to replace non word characters in title column of collections:
console_collection["title"] = console_collection["title"].str.replace(
    "[^\w ]", "", regex=True).astype("str")
pricing["title"].replace(
    to_replace="[^\w ]", value="", regex=True, inplace=True)
### ----- BOTH OF THESE METHODS WORK BUT REMOVE SPACES AS WELL----- ###

### ----- CANNOT GET extract() OR extractall() TO WORK; NEED MORE RESEARCH ----- ###
# Trying out extract:
# console_collection["title"] = console_collection["title"].str.extractall(
#     pat=r"([\w]+)", flags=re.S)
### ----- CANNOT GET extract() OR extractall() TO WORK; NEED MORE RESEARCH ----- ###

### Try to fuzzy match the title names in the data: ###
# Create duplicate column to retain title name from collections:
# console_collection['title'] = df2['team']

# Convert team name in df2 to team name it most closely matches in df1
# console_collection['title'] = console_collection['title'].apply(
#     lambda x: difflib.get_close_matches(x, pricing['title'])[0])


# Merge the new console_collection with the pricing data by fuzzy matching title:
merged_with_prices = pd.merge(
    console_collection, pricing, on="title", how="left")  # INCLUDES ALL GAMES IN LEFT W/OUT PRICING
print(merged_with_prices[["Platform", "title",
      "loose_price", "cib_price", "new_price"]])

# print(merged_with_prices)
# print(merged_with_prices[["title"]])

# Save merged DataFrame into CSV:
merged_with_prices[["Platform", "title",
                    "loose_price", "cib_price", "new_price"]].to_csv(REL_FILE_PATH.joinpath(f"{CONSOLE}_Collection_Pricing.csv"))
