from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("https://www.python.org")
search_bar = wait.until(EC.element_to_be_clickable((By.NAME, 'q')))
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

result = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/li[1]/h3/a')

assert result.text == 'Python For Beginners'

driver.close()



