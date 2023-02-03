import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x_x = x_element.text
    y = calc(x_x)

    text_text = browser.find_element(By.ID, "answer").send_keys(y)

    time.sleep(2)

    robot_1 = browser.find_element(By.ID, "robotCheckbox")
    robot_1.click()

    time.sleep(2)


    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()

    time.sleep(2)

    submit_submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit_submit.click()


finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


