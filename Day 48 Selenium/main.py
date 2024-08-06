from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

n=20

while True:
    cookie = driver.find_element(By.ID, value="cookie")
    money = driver.find_element(By.ID, value="money")
    buy_cursor = driver.find_element(By.ID, value="buyCursor")
    cursor_price=int(buy_cursor.text.split()[2])
    buy_grandma = driver.find_element(By.ID, value="buyGrandma")
    grandma_price=int(buy_grandma.text.split()[2])
    buy_factory = driver.find_element(By.ID, value="buyFactory")
    factory_price=int(buy_factory.text.split()[2])
    buy_mine = driver.find_element(By.ID, value="buyMine")
    mines_price =int(buy_mine.text.split()[2].replace(",",""))
    buy_shipment = driver.find_element(By.ID, value="buyShipment")
    shipment_price=int(buy_shipment.text.split()[2].replace(",",""))
    n+=5
    for i in range(0,n):
        cookie.click()
    curr_money=int(money.text)
    print(curr_money)
    if(curr_money>shipment_price):
        buy_shipment.click()
    elif(curr_money>mines_price):
        buy_mine.click()
    elif (curr_money > factory_price):
        buy_factory.click()
    elif (curr_money > grandma_price):
        buy_grandma.click()
    elif (curr_money > cursor_price):
        buy_cursor.click()
    curr_money = int(money.text)



