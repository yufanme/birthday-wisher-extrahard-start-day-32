# ---------------------------- Extra Hard Starting Project ---------------------------
import pandas
import random
import smtplib
import datetime as dt

EMAIL = "562937707@qq.com"
PASSWORD = "bpyjiqjylklcbdhe"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
data = pandas.read_csv("birthdays.csv")
if month in data.month:
    person = data[data.month == month]
    if person.day.values[0] == day:
        name = person.name.values[0]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
        # with the person's actual name
        # from birthdays.csv
        with open("letter_templates/letter_1.txt") as letter1_file:
            letter1 = letter1_file.read()

        with open("letter_templates/letter_2.txt") as letter2_file:
            letter2 = letter2_file.read()

        with open("letter_templates/letter_3.txt") as letter3_file:
            letter3 = letter3_file.read()

        letters = [letter1, letter2, letter3]
        letter = random.choice(letters)
        print(letter)
        send_letter = letter.replace("[NAME]", name)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.qq.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=f"Subject:Birthday Wish!\n\n{send_letter}")
