import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


button_1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

text_text = browser.find_element(By.ID, 'input_value').text
text_int = int(text_text)
y = calc(text_text)

form_form = browser.find_element(By.ID, 'answer').send_keys(y)
button_2 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()

time.sleep(10)
browser.quit(10)
