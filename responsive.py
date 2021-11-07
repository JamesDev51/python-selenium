from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s,options=options)
browser.maximize_window()
browser.get("https://nomadcoders.co")

sizes=[480,960,1366,1936]
BROWSER_HEIGHT=1056

for size in sizes:
    browser.set_window_size(size,BROWSER_HEIGHT)
    browser.execute_script("window.scrollTo(0,0)")
    sleep(3)
    scroll_size=browser.execute_script("return document.body.scrollHeight")
    total_sections=math.ceil(scroll_size/BROWSER_HEIGHT)
    for section in range(total_sections+1):
        browser.execute_script(f"window.scrollTo(0, {(section+1)*BROWSER_HEIGHT })")
        browser.save_screenshot(f"screenshots/{size}x{section+1}.png")
        sleep(2)