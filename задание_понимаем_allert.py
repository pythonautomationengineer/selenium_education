import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button_1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()

confirm = browser.switch_to.alert
confirm.accept()

text_text = browser.find_element(By.ID, 'input_value').text
text_int = int(text_text)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

new_new = calc(text_int)

pole_pole = browser.find_element(By.ID, 'answer').send_keys(new_new)

button_2 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()

time.sleep(10)