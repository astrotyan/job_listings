# create a text file (with job urls)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

query = 'azure'


driver = webdriver.Chrome()


def get_pages(query):
    # launch the brower
    driver.get(
        'https://careers.microsoft.com/us/en/search-results?keywords='+query)

    # get number of pages
    wait_1stPage = WebDriverWait(driver, 10)
    n_per_page = wait_1stPage.until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="content"]/div/span[1]/span[4]')))
    n_per_page = int(n_per_page.text)
    n_jobs = int(driver.find_element_by_xpath(
        '//*[@id="content"]/div/span[2]').text)

    if n_jobs//n_per_page == 0:
        n_pages = n_jobs//n_per_page
    else:
        n_pages = n_jobs//n_per_page + 1

    # create list of page urls
    pages = [
        f'https://careers.microsoft.com/us/en/search-results?keywords=azure&from={i*20}&s=1' for i in range(n_pages)]

    return(pages)


pages = get_pages(query)
with open(query+'_pages.txt', 'w') as pagefile:
    for page in pages:
        pagefile.write(page+'\n')


def get_urls(pages):
    urls = []
    for page in pages:
        driver.get(page)
        wait_page = WebDriverWait(driver, 10)
        jobs = wait_page.until(EC.presence_of_all_elements_located(
            (By.XPATH,
             '//li[@class="jobs-list-item"]')))
        for job in jobs:
            link = job.find_element_by_xpath('.//a').get_attribute('href')
            urls.append(link)
        time.sleep(random.randint(1, 3))
    return(urls)


urls = get_urls(pages)
with open(query+'_urls.txt', 'w') as urlfile:
    for url in urls:
        urlfile.write(url+'\n')


driver.close()
