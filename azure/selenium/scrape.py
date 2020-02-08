from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

query = 'azure'


def init_csv(query):
    filen = '_'.join(query.split('+'))+'.csv'
    with open(filen, 'w') as csvfile:
        header_writer = csv.writer(csvfile)
        column_names = ['title', 'location', 'job_id', 'date', 'travel', 'profession',
                        'role', 'employment', 'description', 'responsibilites', 'qualifications']
        header_writer.writerow(column_names)
    return(filen)


init_csv(query)


with open('azure_urls.txt', 'r') as f:
    urls = f.readlines()

driver = webdriver.Chrome()


with open(query+'.csv', 'a') as csvfile:
    jobs_writer = csv.writer(csvfile)
    for i, url in enumerate(urls):
        print('Scraping {i} out of {n} jobs'.format(i=i+1, n=len(urls)))
        driver.get(url)
        job = {}
        # column_names = ['title', 'location', 'job_id', 'date', 'travel', 'profession', 'role', 'employment', 'description', 'responsibilites', 'qualifications']
        # title
        wait_job = WebDriverWait(driver, 10)
        title = wait_job.until(EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="content-1"]/div[1]/div/h1')))
        job['title'] = title.text
        # location
        try:
            time.sleep(.5)
            location = [driver.find_element_by_xpath(
                '//*[@id="content-1"]/div[1]/div/div/span').text]
        except:
            location_button = driver.find_element_by_xpath(
                '//*[@id="content-1"]/div[1]/div/div/button')
            location_button.click()
            time.sleep(.5)
            location = []
            locs = driver.find_elements_by_xpath(
                '//*[@id="content-1"]/div[1]/div/ul/li')
            for loc in locs:
                location.append(loc.text)
        job['job_id'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[3]/div/ul/li[1]/span[2]').text
        job['date'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[3]/div/ul/li[2]/span[2]').text
        job['travel'] = driver.find_element_by_xpath(
            '// *[@id="content-1"]/div[3]/div/ul/li[3]/span[2]').text
        job['profession'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[3]/div/ul/li[4]/span[2]').text
        job['role'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[3]/div/ul/li[5]/span[2]').text
        job['employment'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[3]/div/ul/li[6]/span[2]').text
        job['description'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[4]/div[1]').text
        job['responsibilites'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[4]/div[2]/p').text
        job['qualifications'] = driver.find_element_by_xpath(
            '//*[@id="content-1"]/div[4]/div[3]/p').text
        for loc in location:
            job['location'] = loc
            jobs_writer.writerow(job.values())
        if job['title'] == '':
            print('Warning: ', job['job_id'], ' has no title!')
        time.sleep(random.randint(1, 3))

driver.close()
