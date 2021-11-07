from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math
from dotenv import load_dotenv
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s,options=options)
main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

fb_id=os.environ.get("FB_ID")
fb_pw=os.environ.get("FB_PW")

move_facebook_btn =WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME,"yWX7d"))
    ).click()
facebook_id_input =WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.ID,"email"))
    )
facebook_id_input.send_keys(fb_id)
facebook_pw_input =WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.ID,"pass"))
    )
facebook_pw_input.send_keys(fb_pw)
facebook_login_btn =WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.ID,"loginbutton"))
    ).click()
login_success_window =WebDriverWait(browser, 6).until(
    EC.presence_of_element_located((By.CLASS_NAME,"_1XyCr "))
    )

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")


header = browser.find_element_by_tag_name("header")
print(header)

sleep(3000)
browser.quit()