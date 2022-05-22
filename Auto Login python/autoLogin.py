from selenium import webdriver
import time
username = "Barkah"
password = "123"

url = "http://localhost/INV-ukom/login/"
driver = webdriver.Chrome(
    "C:/Users/pc/Documents/ICHOT/Programming/Python/A-DATA/chromedriver.exe")

driver.get(url)
driver.find_element_by_name("id_pengguna").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("btnLogin").click()
time.sleep(2)
