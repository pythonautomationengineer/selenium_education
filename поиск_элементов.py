# Расставим таймаут, чтобы видеть процесс выполнения кода и чтобы браузер не закрывался за мгновение.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button")
time.sleep(2)
browser.quit()
