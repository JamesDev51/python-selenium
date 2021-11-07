from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
KEYWORD = "buy domain"


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s,options=options)

browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

shitty_element =WebDriverWait(browser, 4).until(
    EC.presence_of_element_located((By.CLASS_NAME,"ULSxyf"))
    )
browser.execute_script(
    """
    const shitty = arguments[0];
    shitty.parentElement.removeChild(shitty)
    """,shitty_element)
search_results=browser.find_elements_by_class_name("g")
for index, search_result in enumerate(search_results):
    class_name=search_result.get_attribute("class")
    if "g-blk" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

sleep(200000)
browser.quit()
