from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

first_number = browser.find_element(By.ID, "num1").text
second_number = browser.find_element(By.ID, "num2").text

sum_sum = int(first_number) + int(second_number)  # int с суммой чисел
str_sum = str(sum_sum)  # строка с суммой чисел

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(str_sum)

button_1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()

time.sleep(8)  # есть 8 секунд чтобы скопировать результат
browser.quit()

