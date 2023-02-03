import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


#price_house = browser.find_element_(By.ID, 'price')

find_text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button_1 = browser.find_element(By.ID, 'book').click()


find_button_2 = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", find_button_2) # скроллинг до финальной кнопки


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

find_text_2 = browser.find_element(By.ID, "input_value").text
find_text_2_int = int(find_text_2)
result_function = calc(find_text_2_int)
input_value = browser.find_element(By.ID, 'answer').send_keys(result_function)
button_2 = browser.find_element(By.ID, 'solve').click()


time.sleep(5)
