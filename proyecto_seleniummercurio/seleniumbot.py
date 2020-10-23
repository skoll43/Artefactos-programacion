# proyecto scraper de el mercurio
# elmercurio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import sys

PATH =  r"C:\Users\lukas\Desktop\proyecto python\proyecto_seleniummercurio\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get ("https://digital.elmercurio.com/")
print(driver.title)


print(driver.page_source, file= (file)_Write)