from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

imput_1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)').send_keys("Текст_1")
imput_2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)').send_keys("Текст_2")
imput_3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)').send_keys("email@yandex.ru")

imput_4 = browser.find_element(By.ID, 'file')


current_dir = os.path.abspath(os.path.dirname('__file__'))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'github.txt')           # добавляем к этому пути имя файла

imput_4.send_keys(file_path)

button_1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()

time.sleep(10)