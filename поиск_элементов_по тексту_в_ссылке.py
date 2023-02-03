from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"  # успешно

# link = "http://suninjuly.github.io/registration2.html"  # NoSuchElementException


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.TAG_NAME, "input")
    input_1.send_keys("Иван")

    time.sleep(2)

    input_2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
    input_2.send_keys("Иванов")

    time.sleep(2)

    input_3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
    input_3.send_keys("ivan@ya.ru")

    time.sleep(2)


    input_6 = browser.find_element(By.CSS_SELECTOR, ".btn")
    input_6.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
