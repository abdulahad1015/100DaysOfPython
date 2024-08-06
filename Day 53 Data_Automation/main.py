import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# driver.get("https://forms.gle/gMmRqnwvA2J6Z3uP7")
# fields = driver.find_elements(By.CSS_SELECTOR, value="input")

response = requests.get("https://appbrewery.github.io/Zillow-Clone/",headers=header)
zillow= response.text

soup=BeautifulSoup(zillow,"html.parser")
listing=(soup.findAll(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper"))
for i in listing:

    driver.get("https://forms.gle/gMmRqnwvA2J6Z3uP7")
    time.sleep(2)

    address=i.find(name="address").getText()
    address = address.strip()
    field1 = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field1.send_keys(address)

    price = i.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
    price = price[0:6]
    field2 = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field2.send_keys(price)

    link=i.find(name="a").get("href")
    field3 = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field3.send_keys(link)

    print(address)
    print(price)
    print(link)

    submit=driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
    submit.click()


driver.quit()

# https://docs.google.com/forms/d/e/1FAIpQLSeg15H9Ry2k1SoBLF0PW_iV-Nfh5WQDAcpzyaLXjt3b16jdpw/viewform
# https://docs.google.com/forms/d/e/1FAIpQLSeg15H9Ry2k1SoBLF0PW_iV-Nfh5WQDAcpzyaLXjt3b16jdpw/viewform
