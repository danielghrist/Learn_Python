# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key, value in student_scores.items():
#     if value >= 91:
#         student_grades[key] = "Outstanding"
#     elif value >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif value >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# # 🚨 Do NOT change the code above

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 👇


# def add_new_country(country, num_visits, cities_visited):
#     travel_log.append({
#         "country": country,
#         "visits": num_visits,
#         "cities": cities_visited
#     })


# # 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
