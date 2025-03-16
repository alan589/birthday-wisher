import csv
import datetime as dt
import smtplib
import random
import os

today = dt.datetime.now()

# email
MY_EMAIL = ""
# app password
MY_PASS = ""
# smtp email provider
SMTP = ""

with open("birthdays.csv", "r") as birthday_file:
    birthdays = csv.DictReader(birthday_file)
    for birthday in birthdays:
        birthday_month = int(birthday["month"])
        birthday_day = int(birthday["day"])
        if today.month ==  birthday_month and today.day == birthday_day:
            path = "./letter_templates/"
            files = os.listdir(path)
            random_letter = random.choice(files)
            with open(os.path.join(path + random_letter), "r") as letter_file:
                letter = ''.join(letter_file.readlines())
                birthday_name = birthday["name"]
                letter = letter.replace("[NAME]", birthday_name)

            with smtplib.SMTP(SMTP) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASS)
                birthday_email = birthday["email"]
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_email,
                    msg=f"Subject:Happy Birthday!!!\n\n{letter}"
                )
                print("Email sent!!!")




