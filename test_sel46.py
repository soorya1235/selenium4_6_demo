from selenium import webdriver
from selenium.webdriver.common import selenium_manager 

def test1():  
    abcd = selenium_manager.SeleniumManager.driver_location("chrome")
    print(f"The chrome location is {abcd}")
    print("The chrome locatio nis {}".format(abcd))
    #browser = webdriver.Chrome()
    #browser.get("http://google.com")
    #browser.maximize_window


#download the selenium-manager.exe from the repository

