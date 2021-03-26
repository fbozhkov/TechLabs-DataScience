from urllib.request import urlretrieve
import pandas as pd
import dates
import pathlib
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as selexcept
from datetime import datetime

# PATH = "C:/WebDriver/bin"
currpath = pathlib.Path().absolute()
register_path = str(currpath) + '\Register'
start_date = input("Enter start date: format (y-m-d)")
end_date = input("Enter end date: format (y-m-d)")
assert (type(start_date) == str)
driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe')
# open a given link, maximize window and accept cookies
# Set the link on the page that contains the data from chosen start_date
driver.get('https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv?layout=table&start=0')
driver.maximize_window()
cookies_link = driver.find_element_by_link_text('Einverstanden')
cookies_link.click()
# refresh window because of cookies pop-up hindering clickable area
driver.refresh()

# driver.execute_script("window.scrollBy(0,600)","")
driver.implicitly_wait(5)

date = start_date

start_link = driver.find_element_by_link_text('Start')

# intensive_register = ""
'''
reg_name = 'DIVI-Intensivregister_' + date
reg_xpath = '//a[contains(@aria-label,' + "'" + reg_name + "'" + ' )]'
'''


def find(name, path):
    my_reg_name = name
    my_reg_xpath = path
    my_intensive_register = ""
    for attempt in range(2):
        try:
            print('Trying ' + my_reg_name)
            my_intensive_register = driver.find_element_by_xpath(my_reg_xpath)
        except selexcept.NoSuchElementException:
            print("DIVI file not found on this page: " + my_reg_name)
            back_link = driver.find_element_by_xpath('//*[@title="Zurück"]')
            back_link.click()
        else:
            break
    return my_intensive_register


def click(button):
    intensive_register = button
    try:
        intensive_register.click()
    except:
        print("Could not click " + reg_name)
        driver.implicitly_wait(5)


def save(thisdate):
    try:
        url = driver.current_url
        urlretrieve(url, register_path + '\Intensiveregister_' + thisdate + '.csv')
        print("Saved: " + thisdate)
    except:
        print("Could not save file: " + reg_name)


def savereg(thisdate):
    reg_name = 'DIVI-Intensivregister_' + thisdate
    reg_xpath = '//a[contains(@aria-label,' + "'" + reg_name + "'" + ' )]'
    click(find(reg_name, reg_xpath))
    save(thisdate)


def saveall(sdate, edate):
    thisdate = sdate
    while True:
        savereg(thisdate)
        driver.back()
        thisdate = dates.next_date(thisdate)
        if thisdate == dates.next_date(edate):
            break
    print("Download completed")

    with open('latest_report.txt', 'w') as f:
        f.write(end_date)
    driver.quit()


saveall(start_date, end_date)
''''
        if thisdate != edate:
        savereg(thisdate)
        driver.back()
        thisdate = dates.next_date(thisdate)
    
    for x in range(4):
        savereg(thisdate)
        driver.back()
        thisdate = dates.next_date(thisdate)
'''
# driver.back()
# driver.quit()
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
