# from datetime import datetime
# from os import system
# system('cls')

# current_now = datetime.now()
# current_hour = datetime.now().hour

# print(f"datetime.now() Current Now: {current_now}")
# print(type(f"datetime.now() Type:  {current_now}"))

# print(f"datetime.now().hour Current Hour: {current_hour}")
# print(type(f"datetime.now().hour Type:  {current_hour}"))

# Take a list and return a list of two elements with the first being the sum of the evens numbers and the second being the sum of the odd numbers from the list passed in

# def sum_odd_and_even(data: list) -> list:
#     even_sums = sum([num for num in data if num % 2 == 0])
#     odd_sums = sum([num for num in data if num % 2 != 0])
#     odd_even_sums = [even_sums, odd_sums]
#     return odd_even_sums

# print(sum_odd_and_even([0, 0]))

from requests import api
import os

API_KEY = os.environ.get("OWM_API_KEY")
print(API_KEY)
