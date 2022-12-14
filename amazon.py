from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("apple iphone 13")
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()

product_name=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
price=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]').text




print('Product name is :'+product_name)
print('Price :'+price)

