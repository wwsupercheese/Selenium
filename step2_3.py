from selenium import webdriver
import math
import time

# Функция для вычисления значения капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем браузер и переходим на нужную страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажимаем на кнопку
    button = browser.find_element("tag name", "button")
    button.click()

    # Принимаем confirm-алерт
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ждём перехода на новую страницу
    time.sleep(2)

    # Находим значение x и вычисляем ответ
    x_element = browser.find_element("id", "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    input_field = browser.find_element("id", "answer")
    input_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element("css selector", "button[type='submit']")
    submit_button.click()

    # Получаем текст последнего алерта — это наш результат
    result_alert = browser.switch_to.alert
    print("Результат:", result_alert.text)

finally:
    # Закрываем браузер через 5 секунд, чтобы увидеть результат
    time.sleep(5)
    browser.quit()
