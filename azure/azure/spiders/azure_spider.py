from scrapy import Spider
from azure.items import AzureItem
import re
from selenium import webdriver


class BestBuySpider(Spider):
    name = 'azure_spider'
    allowed_domains = ['careers.microsoft.com']
    start_urls = [
        'https://careers.microsoft.com/us/en/search-results?keywords=azure']

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get(
            'https://careers.microsoft.com/us/en/search-results?keywords=azure')
        n_jobs = driver.find_element_by_xpath(
            '//*[@id="content"]/div/span[2]').text
        driver.close()

        print('*'*60)
        print(n_jobs)
