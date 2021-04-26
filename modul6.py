from selenium import webdriver
import time

url = 'https://fabrykatestow.pl/'
driver = webdriver.Chrome('/home/teresa/PycharmProjects/kurs_fabryka_testow/chromedriver')
#wejsc na strone fabryka testow
driver.get(url)
driver.maximize_window()

#kliknac w kursy
kursy_tab = driver.find_element_by_xpath('//*[@id="menu-item-622"]/a')
kursy_tab.click()

#kliknac kurs testy automatyczne phyton selenium
kurs_phyton_selenium = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a/span/span[2]')
kurs_phyton_selenium.click()

time.sleep(1)

#znalezc informacje kto prowadzi kurs
prowadzacy_kurs = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[2]/div/div/div/div/div/div/h1')
driver.execute_script("arguments[0].scrollIntoView();", prowadzacy_kurs)
#screenshot
image = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img')
image.screenshot('Pawel_Zwierzchowski.png')

driver.quit()

