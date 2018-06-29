from selenium import webdriver
import requests
import bs4
import os
#webscraping with selenium, and using chromedriver
#This script goes into craiglist, and finds the electronics link, and finds
#the xpath element, then the class name hdlnk, then posts all the texts into terminal

chrome_path='/Users/samehphopal/downloads/chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get("http://vancouver.craigslist.com")
driver.find_element_by_xpath("""//*[@id="sss0"]/li[19]/a""").click()
posts = driver.find_elements_by_class_name("hdrlnk")
for post in posts:
    print(post.text)
