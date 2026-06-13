

from selenium import webdriver
import time
navegador = webdriver.Chrome()
time.sleep(2)
navegador.get("https://www.saucedemo.com/")
time.sleep(2)

usuario = navegador.find_element("id", "user-name")
usuario.send_keys("standard_user")

senha = navegador.find_element("id", "password")
senha.send_keys("secret_sauce")

login_button = navegador.find_element("id", "login-button")

navegador.maximize_window()
login_button.click()
time.sleep(5)


