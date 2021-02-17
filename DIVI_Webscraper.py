from urllib.request import urlretrieve
import pandas as pd
import pathlib
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#PATH = "C:/WebDriver/bin"
currpath = pathlib.Path().absolute()
register_path = str(currpath) + '\Register'

driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe')
# open a given link, maximize window and accept cookies
driver.get('https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv?layout=table&start=40')
driver.maximize_window()
cookies_link = driver.find_element_by_link_text('Einverstanden')
cookies_link.click()
# refresh window because of cookies pop-up hindering clickable area
driver.refresh()

#driver.execute_script("window.scrollBy(0,600)","")
driver.implicitly_wait(5)
start_link = driver.find_element_by_link_text('Start')
reg_link = 'DIVI-Intensivregister_2020-05-01_09-15'

reg_path='//a[contains(@aria-label, "DIVI-Intensivregister_2021-01-01" )]'
intensive_register = driver.find_element_by_xpath(reg_path)
intensive_register.click()

url = driver.current_url
urlretrieve(url, register_path + '\Intensiveregister_2021-01-01.csv')
#end_link = driver.find_element_by_xpath('//*[@title="Ende"]')
#dummy_scroll = driver.find_element_by_link_text('Mitglied werden')
#actions = ActionChains(driver)
#actions.move_to_element(start_link).perform()
#dummy_scroll = driver.find_element_by_link_text('Mitglied werden')

#start_link.click()

'''
url = 'https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv/divi-intensivregister-2020-12-20-12-15/viewdocument/5328'

urlretrieve(url, 'intensivecare_12_20.csv')

df = pd.read_csv('intensivecare_12_20.csv', sep=',')

print(df.head())
'''