from urllib.request import urlretrieve
import pandas as pd
import dates
import pathlib
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as selexcept
from datetime import datetime
import sys

# PATH = "C:/WebDriver/bin"
currpath = pathlib.Path().absolute()
register_path = str(currpath) + '\Register'

def run(start, end):
    start_date = start
    end_date = end
    assert (type(start_date) == str)
    date_log = []
    driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver.exe')
    # open a given link, maximize window and accept cookies
    # Set the link on the page that contains the data from chosen start_date
    driver.get('https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv?layout=table&start=0')
    driver.maximize_window()
    cookies_link = driver.find_element_by_link_text('Einverstanden')
    cookies_link.click()
    # refresh window because of cookies pop-up hindering clickable area
    driver.refresh()

    driver.implicitly_wait(5)

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
                try:
                    back_link = driver.find_element_by_xpath('//*[@title="Zurück"]')
                    back_link.click()
                except selexcept.NoSuchElementException:
                    print("DIVI file could not be found")
                    driver.quit()
                    sys.exit(0)
            else:
                break
        return my_intensive_register

    def click(button):
        intensive_register = button

        try:
            intensive_register.click()
        except:
            print("Could not click ")


    def save(thisdate):
        try:
            url = driver.current_url
            urlretrieve(url, register_path + '\Intensiveregister_' + thisdate + '.csv')
            date_log.append(thisdate)
            print("Saved: " + date_log[-1])
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

today = datetime.today().strftime('%Y-%m-%d')

with open('latest_report.txt', 'r') as f:
    last_update = f.read()

if today == last_update:
    print('Dataset up to date')
else:
    print('Downloading latest reports...')
    run(last_update, today)

