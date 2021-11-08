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
service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service,options=options)
main_galleries=["fashion70","fashion_q",""]

browser.get("https://gall.dcinside.com/board/write/?id=pants")
sleep(1)
id=browser.find_element(by="id",value="name")
id.send_keys("ㅇㅇ")
password=browser.find_element(by="id",value="password")
password.send_keys("1234")
password=browser.find_element(by="id",value="subject")

browser.switch_to.frame("tx_canvas_wysiwyg")
paragraph=browser.find_element_by_tag_name("p")
# paragraph.send_keys("1dddddd")
print(paragraph)
browser.execute_script(
    """
    const p = arguments[0];
    p.innerHTML="dddddd"
    """,
    paragraph
)
browser.switch_to.default_content()
browser.execute_script(
    """
    const btn = document.querySelector("#tx_image");
    console.log(btn);
    const child = btn.querySelector("a");
    console.log(child);
    child.click()
    """
)
browser.switch_to.active_element
sleep(3)
browser.switch_to.window(browser.window_handles[-1])
sleep(3)

file_add_btn =WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME,"file_add"))
    )
file_add_btn.send_keys(r"C:\Users\alstj\OneDrive\사진\Saved Pictures\test.PNG")
fild_add_complete_btn=WebDriverWait(browser, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME,"btn_apply"))
    ).click()
# write_btn_click=browser.execute_script(
#     """
#     const btn = document.getElementById("btn_write");
#     console.log(btn);
#     btn.click();
#     """)
sleep(2000)