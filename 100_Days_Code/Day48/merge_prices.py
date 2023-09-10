'''
Script to merge my personal collection with the price data I have scraped to get up to date pricing info so I know what is worth selling and what isn't.
'''
import pandas as pd
import difflib
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

# Print first few lines of each new DataFrame:
# print(collection.head())
# print(pricing.head())

# Create DataFrame with only includes the CONSOLE I want to view prices for:
console_collection = collection.query(f"Platform == '{CONSOLE}'")


# Rename the Title column header in the collection data to match the pricing data:
console_collection.rename(columns={"Title": "title"}, inplace=True)
# print(console_collection)

### Try to fuzzy match the title names in the data: ###
# Create duplicate column to retain title name from collections:
# console_collection['title'] = df2['team']

# Convert team name in df2 to team name it most closely matches in df1
# console_collection['title'] = console_collection['title'].apply(
#     lambda x: difflib.get_close_matches(x, pricing['title'])[0])


# Merge the new console_collection with the pricing data by fuzzy matching title:
merged_with_prices = pd.merge(console_collection, pricing, on="title", )
print(merged_with_prices[["Platform", "title",
      "loose_price", "cib_price", "new_price"]])

merged_with_prices[["Platform", "title",
                    "loose_price", "cib_price", "new_price"]].to_csv("Wii_Collection_Pricing.csv")
