from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')

driver.implicitly_wait(time_to_wait=10)