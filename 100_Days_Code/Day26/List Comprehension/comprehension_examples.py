# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# sentence = sentence.replace("?", "")
# print(sentence)
# word_list = [word for word in sentence.split()]
# print(word_list)
# result = {word: len(word) for word in word_list}
#
# for key in result.items():
#     print(key)

# DICTIONARY COMPREHENSION WITH .ITEMS()
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# # new_dict = {new_key: new_value for (key, value) in dict.items()}
# weather_f = {key: round((value * 1.8) + 32), 2) for (key, value) in weather_c.items()}
#
# print(weather_f)
# END OF DICTIONARY COMPREHENSION WITH .ITEMS()

# DAY 26 END INTERACTIVE EXAMPLE DICTIONARY COMPREHENSION
# #For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# #List Comprehension
# new_list = [n + 1 for n in numbers]
#
# #String as List
# name = "Angela"
# letters_list = [letter for letter in name]
#
# #Range as List
# range_list = [n * 2 for n in range(1, 5)]
#
# #Conditional List Comprenhension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
#
# upper_case_names = [name.upper() for name in names if len(name) > 4]
#
# #Dictionary Comprehension
# import random
# student_grades = {name: random.randint(1, 100) for name in names}
# print(student_grades)
#
# passed_students = {
#     student: grade
#     for (student, grade) in student_grades.items() if grade >= 60
# }
# print(passed_students)
# END OF DAY 26 END INTERACTIVE EXAMPLE DICTIONARY COMPREHENSION


# DAY 26 FINAL EXAMPLE ITERATE OVER A PANDAS DATAFRAME
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# FOR LOOP TO LOOP THROUGH KEYS AND VALUES
# for (key, value) in student_dict.items():
#     print(value)

# LOOPING THROUGH PANDAS DATAFRAME
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# for (key, value) in student_dataframe.items():
#     print(key, value)

# PANDAS BUILT IN METHOD TO LOOP THROUGH DATAFRAME
for (index, row) in student_dataframe.iterrows():
    if row.score == 56:
        print(row)








