from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.113 Safari/537.36')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com")
time.sleep(40) 


group_name = "Gen AI - Webinar"
driver.find_element(By.XPATH, f"//span[@title='{group_name}']").click()
time.sleep(10)

title = driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div[2]/span')
numbers = title.get_attribute('title')
numbers = [num.strip() for num in numbers.split(",") if num.strip().startswith("+")]
print(numbers)
numbers = pd.DataFrame(numbers,columns=['phone_number'])
numbers.to_excel(f'{group_name}_numbers.xlsx',index=False)
driver.quit()