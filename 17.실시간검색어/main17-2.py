import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = 'https://zum.com'
driver.get(url = URL)
driver.implicitly_wait(time_to_wait=10)

# driver.find_element(By.CSS_SELECTOR,'#search-input').send_keys("아무거나")
# time.sleep(0.5)

# driver.find_element(By.CSS_SELECTOR,'#app > div > header > div.search_bar > div > fieldset > div > button.search').click()
# time.sleep(1)

zoom_results= driver.find_elements(By.CSS_SELECTOR,'#app > div > header > div.gnb_wrap > div > div > div.issue_wrap > div > div.list_wrap.issue_type')

zoom_list = []
for zoom_result in zoom_results:
    print(zoom_result.text)
    zoom_list.append(zoom_result.text)


print("줌", zoom_list)