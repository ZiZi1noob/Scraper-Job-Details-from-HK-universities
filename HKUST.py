from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NLP import filter

def HKUST(driver, dic):
    driver.execute_script('return document.body.scrollHeight')
    text_link_list = driver.find_elements(By.XPATH, '//a[@class="job-link"]')
    text_link_box = []
    for index in range(len(text_link_list)):
        text_link_box.append(text_link_list[index].get_attribute('href'))

    for index in range(len(text_link_box)):
        url = text_link_box[index]
        driver.get(url)
        time.sleep(5)
        text = driver.find_element(By.XPATH, '//div[@id="job-content"]').text
        if filter(text) != []:
            dic['University'].append('University of Hong Kong')
            dic['Job Details'].append(text)
            dic['URL'].append(url)
    
    return dic
        


