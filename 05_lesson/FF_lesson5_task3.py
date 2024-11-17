from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")


search_input_user = driver.find_element(By.ID, "username")
search_input_user.send_keys("tomsmith", Keys.ENTER)
search_input_password = driver.find_element(By.ID, "password")
search_input_password.send_keys("SuperSecretPassword!", Keys.ENTER)



driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in").click()


sleep(5)

driver.quit()