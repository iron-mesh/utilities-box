from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get(r"https://free.drweb.ru/download+cureit+free/")
browser.execute_script("document.getElementById('Iagree').checked = true")

browser.find_element(by=By.CLASS_NAME, value="js_ya_ga_click_free_download").click()

#stage 2
name = browser.find_element(value="popup-form_name")
surname = browser.find_element(value="popup-form_surname")
e_mail = browser.find_element(value="popup-form_email")

name.send_keys("Илья")
surname.send_keys("Смирнов")
e_mail.send_keys("otherivan@gmail.com")
browser.execute_script("document.getElementById('I_agree').checked = true")
e_mail.submit()
browser.close()