from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')

driver.implicitly_wait(time_to_wait=10)
titles = driver.find_elements(By.CSS_SELECTOR,'#revolution_main_table > tbody > tr:nth-child(9) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')

for title in titles:
    print(title.text)
