from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s,options=options)
browser.maximize_window()
browser.get("https://nomadcoders.co")

sizes=[320,480,960,1366,1936]


for size in sizes:
    browser.set_window_size(size,1056)
    sleep(3)
print(3)