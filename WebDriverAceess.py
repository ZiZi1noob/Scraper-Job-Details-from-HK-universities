from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def WebDriverAcess(url):
    #acess to chromedriver
    options = Options()
    #options.headless = True
    #options.addArguments("--disable-notifications")
    #driver = webdriver.Chrome("./chromedriver_mac_v103") #mac path
    driver = webdriver.Chrome("./chromedriver_win_v103", options = options) #wind path
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    print('webdriver looks good!!!!!')
    return driver