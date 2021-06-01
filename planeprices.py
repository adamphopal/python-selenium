from selenium import webdriver
import requests
import bs4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time
import os


class expediaUnitTest():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--incognito")
        chrome_path = '/Users/samehphopal/downloads/chromedriver'
        driver = webdriver.Chrome(chrome_path)
 #       os.environ["webdriver.chrome.driver"] = driver
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)


    def timerPractice(self):
        time.sleep(10)


    def gotoexpedia(self):
        self.driver.get("http://www.expedia.com")
        timeout = 10
        ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, "tab-flight-tab-hp")))
                
        self.driver.find_element_by_id("tab-flight-tab-hp").click()
       

        ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, "flight-orgin-hp")))

        self.driver.find_element_by_id("flight-orgin-hp-flight").send_keys('Los Angeles, United States of America (QLA)')

        self.driver.find_element_by_id("flight-destination-hp-flight").send_keys('Seattle, WA (SEA)')
        self.driver.find_element_by_id("flight-departing-hp-flight").send_keys('06/21/2018')
        self.driver.find_element_by_id("flight-returning-hp-flight").send_keys('06/26/2018')
        self.driver.find_element_by_id("flight-travelers").send_keys('1 Traveler')

        self.driver.find_element_by_id("search-button-hp-package").click()

 #       self.driver.quit()
        
        parentTab = self.driver.find_element_by_id('flightModuleList')
        for selectAll in parentTab.find_elements_by_xpath("//*"):
            if selectAll.get_attribute("class") == 'dollars price-emphasis':
                print(selectAll.get_attribute("class"))
                print(selectAll.text)

    

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    obj = expediaUnitTest()
    obj.gotoexpedia()
    

