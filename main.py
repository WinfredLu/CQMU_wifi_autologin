'''
注意
该脚本通过调用WebDriver和Selenium软件包来执行自动填充和登录功能。
运行脚本前，请确保以上软件包正确安装，并将脚本内将提示文字替换为你的账密。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://172.31.85.101")
wait = WebDriverWait(driver, 10)


def find_and_clear_input(selector, text):
    try:
        # 等待元素可见并清空输入框
        element = wait.until(EC.visibility_of_element_located(selector))
        element.clear()
        element.send_keys(text)
    except TimeoutException:
        print(f"元素 {selector} 未找到或不可交互。")


def click_element(selector):
    try:
        # 等待元素可点击并点击
        element = wait.until(EC.element_to_be_clickable(selector))
        element.click()
    except TimeoutException:
        print(f"元素 {selector} 未找到或不可交互。")


find_and_clear_input((By.ID, "username"), "在此输入账户")
password_script = "document.getElementById('pwd').value = arguments[0];"
driver.execute_script(password_script, "在此输入密码")
click_element((By.ID, "selectDisname"))
click_element((By.XPATH, "//div[contains(text(),'中国移动')]"))
click_element((By.ID, "loginLink"))

driver.quit()
