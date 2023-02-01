from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(1) > input:nth-child(2)')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(2) > input:nth-child(2)')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла