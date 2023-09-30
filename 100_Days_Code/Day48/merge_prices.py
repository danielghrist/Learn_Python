'''
Script to merge my personal collection data with the price data I have scraped to get up to date pricing info on each game so I know what is worth selling and what isn't.
@author: Daniel Ghrist
'''

import pandas as pd
# import difflib  # Used to mess with fuzzy matching
from pathlib import Path

# Console to get prices for:
CONSOLE = "Wii"

# Create a path to where we are running this script from to find data files:
REL_FILE_PATH = Path(__file__, "../").resolve()

# Create constants for csv files to read in:
PRICING_FILE_NAME = "2023_09_30-Wii-Price_List.csv"
COLLECTION_FILE_NAME = "2023_09_30-iCollect Everything Collection.csv"

# Load personal collection data as Pandas DataFrame:
collection = pd.read_csv(REL_FILE_PATH.joinpath(COLLECTION_FILE_NAME))

# Load pricing data as Pandas Dataframe:
pricing = pd.read_csv(REL_FILE_PATH.joinpath(PRICING_FILE_NAME))

# Create DataFrame which only includes the CONSOLE I want to view prices for:
console_collection = collection.query(f"Platform == '{CONSOLE}'").reset_index()

# Rename the Title column header in the collection data to match the pricing data:
# console_collection.rename(columns={"Title": "title"}, inplace=True)


### ----- BOTH OF THESE METHODS WORK BUT REMOVE SPACES AS WELL----- ###
### ----- FIXED SPACING ISSUE WITH REGEX [^\w ] ----- ###

# Attempting to create a new column in each DataFrame to merge on:
console_collection["Merged_Title"] = console_collection["Title"].str.replace(
    r"[ ][aA]nd[ ]", "", regex=True).str.replace(r"[\W]", "", regex=True).str.upper()
pricing["Merged_Title"] = pricing["title"].str.replace(
    r"[ ][aA]nd[ ]", "", regex=True).str.replace(r"[\W]", "", regex=True).str.upper()

### ----- CHECKING TO SEE WHAT NAMES CERTAIN GAMES ARE IN EACH DF ----- ###
word = "JUON"
filt = pricing["Merged_Title"].str.contains(word)
print(pricing.loc[filt, ["Merged_Title", "cib_price"]])
filt1 = console_collection["Merged_Title"].str.contains(word)
print(console_collection.loc[filt1, "Merged_Title"])
### ----- END CHECKING TO SEE WHAT NAMES CERTAIN GAMES ARE IN EACH DF ----- ###

# # Replace & with "And" in console_collection:
# console_collection["title"] = console_collection["title"].str.replace(
#     "&", "And", regex=True)

# # Replace "-" with " " in pricing Dataframe:
# pricing["title"] = pricing["title"].str.replace(
#     "-", " ", regex=True)

# # Using str.replace with regex to replace non word characters in title column of collections:
# console_collection["title"] = console_collection["title"].str.replace(
#     "[^\w ]", "", regex=True)

# pricing["title"].replace(
#     to_replace="[^\w ]", value="", regex=True, inplace=True)

# # Replace duplicate spaces with just one space:
# console_collection["title"] = console_collection["title"].str.replace(
#     "[ ]{2}", " ", regex=True).astype("str")
# pricing["title"] = pricing["title"].str.replace(
#     "[ ]{2}", " ", regex=True)

# # Title Case both Dataframes "title" column:
# console_collection["title"] = console_collection["title"].str.title()
# pricing["title"] = pricing["title"].str.title()
### ----- END BOTH OF THESE METHODS WORK BUT REMOVE SPACES AS WELL----- ###


### ----- CANNOT GET extract() OR extractall() TO WORK; NEED MORE RESEARCH ----- ###
# Trying out extract:
# console_collection["title"] = console_collection["title"].str.extractall(
#     pat=r"([\w]+)", flags=re.S)
### ----- END CANNOT GET extract() OR extractall() TO WORK; NEED MORE RESEARCH ----- ###

### ----- TRYING TO MESS WITH FUZZY MATCHING THE TITLE NAMES IN THE DATA -----###
# Create duplicate column to retain title name from collections:
# console_collection['title'] = df2['team']

# Convert team name in df2 to team name it most closely matches in df1
# console_collection['Merged_Title'] = console_collection['Merged_Title'].apply(
#     lambda x: difflib.get_close_matches(x, pricing['Merged_Title'])[0])
# print(console_collection["Merged_Title"])
### ----- END TRYING TO MESS WITH FUZZY MATCHING THE TITLE NAMES IN THE DATA -----###


# Merge the new console_collection with the pricing data by matching title:
merged_with_prices = pd.merge(
    console_collection, pricing, on="Merged_Title", how="left")  # ALL GAMES IN LEFT W/OUT PRICING

# print(merged_with_prices[["Platform", "Merged_Title",
#       "loose_price", "cib_price", "new_price"]])

filt = merged_with_prices["title"].isna()
print(merged_with_prices.loc[filt, [
      "title", "Title", "Merged_Title", "cib_price"]])
print(merged_with_prices["title"].isna().value_counts())
print(merged_with_prices["Title"].isna().value_counts())
print(pricing[["title", "Merged_Title"]])

merged_with_prices.loc[merged_with_prices["PC_ID"].isna(), 'PC_ID'] = 0
# merged_with_prices.loc[merged_with_prices["PC_ID"].str.contains(
# ".0"), 'PC_ID'.replace(".0", "")] = merged_with_prices["PC_ID"].replace(".0", "")
merged_with_prices["PC_ID"] = merged_with_prices["PC_ID"].astype(dtype='str')

# Save merged DataFrame into CSV:
merged_with_prices[["Platform", "PC_ID", "Merged_Title",
                    "loose_price", "cib_price", "new_price"]].to_csv(REL_FILE_PATH.joinpath(f"{CONSOLE}-Collection_Pricing.csv"), lineterminator="\n", encoding="utf8")
