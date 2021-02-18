from urllib.request import urlretrieve
import pandas as pd
import pathlib
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# PATH = "C:/WebDriver/bin"
currpath = pathlib.Path().absolute()
register_path = str(currpath) + '\Register'
start_date = input("Enter start date: format (y-m-d)")
assert (type(start_date) == str)

driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe')
# open a given link, maximize window and accept cookies
driver.get('https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv?layout=table&start=40')
driver.maximize_window()
cookies_link = driver.find_element_by_link_text('Einverstanden')
cookies_link.click()
# refresh window because of cookies pop-up hindering clickable area
driver.refresh()

# driver.execute_script("window.scrollBy(0,600)","")
driver.implicitly_wait(5)

date = start_date

start_link = driver.find_element_by_link_text('Start')
back_link = driver.find_element_by_link_text('Zurück')
# intensive_register = ""

reg_name = 'DIVI-Intensivregister_' + date
reg_xpath = '//a[contains(@aria-label,' + "'" + reg_name + "'" + ' )]'


def find(name, path):
    my_reg_name = name
    my_reg_xpath = path
    my_intensive_register = ""
    try:
        my_intensive_register = driver.find_element_by_xpath(my_reg_xpath)
    except:
        print("DIVI file not found:" + my_reg_name)
    return my_intensive_register


def click(button):
    intensive_register = button
    try:
        intensive_register.click()
    except:
        print("Could not click " + reg_name)


def save():
    try:
        url = driver.current_url
        urlretrieve(url, register_path + '\Intensiveregister_' + date + '.csv')
    except:
        print("Could not save file: " + reg_name)

driver.quit()
# end_link = driver.find_element_by_xpath('//*[@title="Ende"]')
# dummy_scroll = driver.find_element_by_link_text('Mitglied werden')
# actions = ActionChains(driver)
# actions.move_to_element(start_link).perform()
# dummy_scroll = driver.find_element_by_link_text('Mitglied werden')

# start_link.click()

'''
url = 'https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv/divi-intensivregister-2020-12-20-12-15/viewdocument/5328'

urlretrieve(url, 'intensivecare_12_20.csv')

df = pd.read_csv('intensivecare_12_20.csv', sep=',')

print(df.head())
'''
