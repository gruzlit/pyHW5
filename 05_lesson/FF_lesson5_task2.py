from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()


driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("1000", Keys.ENTER)
sleep(5)

search_input.clear()


search_number = driver.find_element(By.CSS_SELECTOR, "input")
search_number.send_keys("999", Keys.ENTER)

sleep(5)
driver.quit()