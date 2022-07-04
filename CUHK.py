from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NLP import filter, content_stem

def CUHK(driver, dic):
    job_title_btn = driver.find_element(By.XPATH, "//input[@id='JOB_TITLE']")
    job_title_btn.clear()
    time.sleep(0.5)
    job_title_btn.send_keys('Research Assistant')
    time.sleep(0.5)
    job_title_btn.send_keys(Keys.ENTER)
    time.sleep(0.5)
    job_link_box = []

    #obtain each link for each job position
    while 1:
        job_body = driver.find_element(By.XPATH, '//tbody[@class="jobsbody"]').find_elements(By.XPATH, 'tr/td[2]/div[1]/div[1]/span[1]/a')
        
        #get all urls
        for index in range(len(job_body)):
            job_link_box.append(job_body[index].get_attribute('href'))

        #click into next page
        next_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Next')]")
        if next_btn.get_attribute('aria-disabled') != 'true':
            next_btn.click()
            time.sleep(2)
        else:
            break

    #access to each job url
    for index in range(len(job_link_box)):
        url = job_link_box[index]
        driver.get(url)
        time.sleep(5)
        text = driver.find_element(By.XPATH, '//div[@id="requisitionDescriptionInterface"]').text
        if filter(content_stem(text)) != []:
            dic['University'].append('Chinese University of Hong Kong')
            dic['Job Details'].append(text)
            dic['URL'].append(url)
    
    return dic
        


