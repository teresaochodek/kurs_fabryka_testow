from selenium import webdriver
import time

driver = webdriver.Chrome('homeworks/chromedriver')

driver.get('https://google.pl')

# search.box = driver.find_element_by_name('q')
# search.box.send_keys('selenium phyton')
# search.box.submit()
# time.sleep(5)
# driver.quit

