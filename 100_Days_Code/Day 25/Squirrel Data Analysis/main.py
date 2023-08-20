import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"].value_counts())

new_dataframe = pandas.DataFrame(data["Primary Fur Color"].value_counts())
print(new_dataframe)
new_dataframe.to_csv("Squirrel Color Counts.csv")