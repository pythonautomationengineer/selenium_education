import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")

    y = calc(x_element)

    text_text = browser.find_element(By.ID, "answer").send_keys(y)

    robot_1 = browser.find_element(By.ID, "robotCheckbox")
    robot_1.click()


    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()


    submit_submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
    submit_submit.click()


finally:

    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

