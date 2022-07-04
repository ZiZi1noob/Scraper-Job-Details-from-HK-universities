from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from NLP import filter, content_stem

def PolyU(driver, dic):

    job_link_box = []
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    job_links = driver.find_elements(By.XPATH, '//tr[@class="ITS_clickableTableRow"]')
    
    #obtain each link for each job position
    for index in range(len(job_links)):
            url = 'https://jobs.polyu.edu.hk/' + job_links[index].get_attribute('data-href')
            job_link_box.append(url)


    #access to each job url
    for index in range(len(job_link_box)):
        url = job_link_box[index]
        driver.get(url)
        time.sleep(5)
        text = driver.find_element(By.XPATH, '//div[@class="wrapper"]').text
        if filter(content_stem(text)) != []:
            dic['University'].append('Hong Kong Polytech U')
            dic['Job Details'].append(text)
            dic['URL'].append(url)
    
    return dic
        


