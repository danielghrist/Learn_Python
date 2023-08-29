import pandas as pd

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"].value_counts())

# new_dataframe = pandas.DataFrame(data["Primary Fur Color"].value_counts())
# print(new_dataframe)
# new_dataframe.to_csv("Squirrel Color Counts.csv")

data = pd.read_csv(
    "./100_Days_Code/Day 25/Squirrel Data Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(type(data))

# Find number of NaN, Null, or None entries in the Primary Fur Color column:
# data = data["Primary Fur Color"].isnull().value_counts()
# print(data)

# Find number squirrel by color:
# data = data["Primary Fur Color"].dropna(
# ).value_counts().reset_index(name="Fur Color")
data = data["Primary Fur Color"].value_counts(dropna=False).reset_index()
data.columns = ["Fur Color", "Count"]
# data = pd.value_counts(data["Primary Fur Color"], dropna=False)
# data = pd.DataFrame(data)
# data.set_axis(["Fur Color"], axis="columns", inplace=True) # Rename columns
# data = data["Primary Fur Color"].isnull().value_counts()
print(type(data))
print(data)
