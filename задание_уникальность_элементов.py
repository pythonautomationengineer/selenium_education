import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    text_link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    text_link.click()

    input_1 = browser.find_element(By.TAG_NAME, "input")
    input_1.send_keys("Петров")

    input_2 = browser.find_element(By.NAME, "last_name")
    input_2.send_keys("Петр")

    input_3 = browser.find_element(By.CLASS_NAME, "city")
    input_3.send_keys("Казань")

    input_4 = browser.find_element(By.ID, "country")
    input_4.send_keys("Россия")

    input_5 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input_5.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла