from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
def summa(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    summa1 = summa(num1, num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта, вот би всё работало
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

