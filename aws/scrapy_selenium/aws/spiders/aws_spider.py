from scrapy import Spider
from aws.items import AwsItem
import re


class AwsSpider(Spider):
    name = 'aws_spider'
    allowed_urls = ['https://www.amazon.jobs/en']
    start_urls = [
        'https://www.amazon.jobs/en/search.json?base_query=aws&city=&country=&county=&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_function_id&latitude=&loc_group_id=&loc_query=&longitude=&offset=0&query_options=&radius=24km&region=&result_limit=10&sort=relevant&offset=0']

    def parse(self, response):
        test = response
        print('*'*60)
        print(type(test))
