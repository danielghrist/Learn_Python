# import smtplib
#
import smtplib
import random
import datetime as dt
my_email = "dannyghrist@gmail.com"
password = "ILoveOracle1!"
#
# with smtplib.SMTP("smtp.gmail.com") as connection
#     # **Secures connection**
#     connection.starttls()
#     #***********************
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="danielghrist@gmail.com",
#                         msg="Subject:Hello... Test\n\nThis is the body of my email.")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year == 2021:
#     print("Wear a face mask")
#
# date_of_birth = dt.datetime(year=1984, month=7, day=19, hour=4)
#
# print(date_of_birth)
# print(year)
# print(type(year))


# ***** SEND AN EMAIL WITH A RANDOM INSPIRATION QUOTE FROM QUOTES.TXT IF THE WEEKDAY IS TUESDAY*****

with open("quotes.txt", "r") as df:
    quotes = df.readlines()

if dt.datetime.now().weekday() == 1:
    random_quote = random.choice(quotes)
    quote_line_list = random_quote.split("\" ")

    # Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="danielghrist@gmail.com",
                            msg=f"Subject:Inspirational Quote of the Week\n\n{quote_line_list[0]}\"\n{quote_line_list[1]}")

#
#
#
