# import csv
#
# # with open("./weather_data.csv") as weather_csv:
# #     data = weather_csv.readlines()
# #     print(data)
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#  temperatures = []
#  for row in data:
#      if row[1] != "temp":
#          temperatures.append(int(row[1]))
#  print(temperatures)
# OR
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
# print(data.to_html)
# print(type(data["temp"]))
# print(data)

# temp_list = data["temp"].to_list()
# print(data["temp"].max())
# print(data.temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# def celcius_to_farenheit(celcius_temp):
#     return celcius_temp * 1.8 + 32
#
# monday = data[data.day == "Monday"]
# Invoke a function on value of Series
# print(monday.temp.apply(func=celcius_to_farenheit))

# Create a Dataframe from scratch
created_data = pandas.DataFrame(data_dict)
print(created_data)

created_data.to_csv("new_data.csv")
