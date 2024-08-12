from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os
from dotenv import load_dotenv, find_dotenv
from random import random
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class InstaFollower:
    def __init__(self):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.EMAIL = os.getenv("INSTA_EMAIL")
        self.PASSWORD = os.getenv("INSTA_PASSWORD")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com/dp/B075CYMYK6?th=1")
        self.followers=[]
        time.sleep(12)
        username = self.driver.find_element(By.ID, value="username1")
        for i in self.EMAIL:
            username.send_keys(i)
            time.sleep(random(0,10)/10)

    def login(self):
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(self.EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(self.PASSWORD, Keys.ENTER)
        time.sleep(10)
        not_now = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        not_now.click()
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH, "//button[text()='Not Now']")
        not_now.click()
        time.sleep(1)
        # search_icon = self.driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Search']")
        # search_icon.click()
        # time.sleep(0.5)
        # search_box = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search input']")
        # search_box.send_keys("Lando Norris",Keys.ENTER)
        # time.sleep(2)
        # search_box.send_keys(Keys.DOWN,Keys.ENTER)

    def find_accounts(self):
        self.driver.get("https://www.instagram.com/landonorris/followers/")
        time.sleep(3)
        followers = self.driver.find_element(By.CSS_SELECTOR, "a[href='/landonorris/followers/']")
        followers.click()
        time.sleep(5)
        for i in range(1,5):
            self.followers.append(self.driver.find_element(By.XPATH,f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button/div/div"))
        time.sleep(5)

    def follow(self):
        for i in self.followers:
            i.click()
            time.sleep(2)

a=InstaFollower()
# a.login()
# a.find_accounts()
# a.follow()

# /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button/div/div
# /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/button/div/div
# /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div/button/div/div