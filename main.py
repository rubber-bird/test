from time import sleep
from selenium import webdriver
from application.application import Application
if __name__ == '__main__':
    driver = webdriver.Chrome()
    app = Application(driver)
    driver.get("http://www.google.com")
    sleep(5)
    driver.quit()
