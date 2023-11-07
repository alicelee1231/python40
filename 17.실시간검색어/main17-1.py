from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome()

URL = 'https://www.google.co.kr'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)