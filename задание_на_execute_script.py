import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()

link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_x = browser.find_element(By.ID, 'input_value').text  # найденный текст
x_x_x = int(x_x)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x_x_x)

input_input = browser.find_element(By.ID, 'answer').send_keys(y)

im_robot = browser.find_element(By.ID, 'robotCheckbox').click()


button = browser.find_element(By.TAG_NAME, 'input')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

robots_rule = browser.find_element(By.ID, 'robotsRule').click()
submit_submit = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()

time.sleep(10)



