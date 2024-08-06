import os
import smtplib

from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import requests
import lxml

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
response = requests.get("https://appbrewery.github.io/instant_pot/", headers={"Accept-Language": "en-US"})

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
price = float(soup.find(name="span", class_="a-price-whole").text)
fraction = float(soup.find(name="span", class_="a-price-fraction").text)
price += fraction / 100

if (price < 90):
    SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
    my_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    connection = smtplib.SMTP(SMTP_ADDRESS, port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abdulahad1017@outlook.com",
                        msg="Subject:Price Dropped\n\nPrice has dropped below 99")
print((price))
