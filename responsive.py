from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math

class ResponsiveTester:
    def __init__(self,urls,):
        self.options=webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.s=Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.s,options=self.options)
        self.browser.maximize_window()
        self.urls=urls
        self.sizes=[480,960,1366,1936]
        self.BROWSER_HEIGHT=1056
    def screenshot(self,url):
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size,self.BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            sleep(3)
            scroll_size=self.browser.execute_script("return document.body.scrollHeight")
            total_sections=math.ceil(scroll_size/self.BROWSER_HEIGHT)
            for section in range(total_sections+1):
                self.browser.execute_script(f"window.scrollTo(0, {(section+1)*self.BROWSER_HEIGHT })")
                self.browser.save_screenshot(f"screenshots/{size}x{section+1}.png")
                sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

tester=ResponsiveTester(["https://nomadcoders.co","https://google.com"])
tester.start()