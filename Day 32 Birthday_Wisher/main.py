import smtplib
import datetime as dt
import random
import pandas


my_email = "abdulahad1015@gmail.com"
password = "***********************"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
weekday = now.weekday()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letters=[]
wish=[]
with open("letter_templates/letter_1.txt") as file:
    letters.append(file.read())
with open("letter_templates/letter_2.txt") as file:
    letters.append(file.read())
with open("letter_templates/letter_3.txt") as file:
    letters.append(file.read())
birthdays=pandas.read_csv("birthdays.csv")
birthday_dict=birthdays.to_dict(orient="records")
for i in birthday_dict:
    if(i['month']==now.month and i['day']==now.day):
        wish.append(i)

if len(wish) !=0:
    for i in wish:
        message=random.choice(letters)
        message=message.replace("[NAME]",i['name'])
        print(message)
        connection.sendmail(from_addr=my_email, to_addrs="abdulahad1017@outlook.com",msg=f"Subject:Happy Birthday {i['name']}\n\n{message}")


# 4. Send the letter generated in step 3 to that person's email address.



connection.close()