##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
from _datetime import datetime
import random
import pandas


my_email = "dannyghrist@gmail.com"
password = "ILoveOracle1!"

# IMPORT BIRTHDAYS FROM DATA FILE
try:
    data = pandas.read_csv("birthdays.csv")

except FileNotFoundError:
    quit()
# -----------------------------------

# CHECK IF TODAY'S DATE MATCHES ANY BIRTHDAYS IN THE CSV FILE
now = datetime.now()
today = (now.month, now.day)

# birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

# NOTE TO SELF:
# iterrows() iterates through the rows of a pandas DataFrame object and returns tuple of (index, panda Series)
# Could also use itertuples() which per the documentation preserves dtypes and is faster
for row in data.iterrows():
    if (row[1]["month"], row[1]["day"]) == today:
        print(f"Today is your birthday {row[1]['name']}")
        birthday_person = row[1]["name"]
        age = now.year - row[1]["year"]
        file_path = (f"letter_templates/letter_{random.randint(1, 3)}.txt")
        with open(file_path) as letter_file:
            contents = letter_file.read()
            message = contents.replace("[NAME]", row[1]["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row[1]["email"],
                                msg=f"Subject:Happy {age} Birthday\n\n"
                                    f"{message}")


# for row in data.itertuples():
#     print(row)
#     print(row[2])

# -------------------------------------






