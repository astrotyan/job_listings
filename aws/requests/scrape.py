import requests
import json
import csv
import time
import random
import re


def get_urls_filename(query):
    pre_url = 'https://www.amazon.jobs/en/search.json?radius=24km&facets[]=location&facets[]=business_category&facets[]=schedule_type_id&facets[]=employee_class&facets[]=normalized_location&facets[]=job_function_id&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&city=&country=&region=&county=&query_options=&base_query='+query
    url_1stPage = pre_url+'&facets[]=category'+'&offset=0'

    # the response is in json format
    # .json() converts the json content to a dict
    data_1stPage = requests.get(url_1stPage).json()

    # data_1stPage.keys()
    # dict_keys(['error', 'hits', 'facets', 'jobs'])

    # 'hits' stores the total number of rearch results
    # can only access 10000 jobs
    n_jobs = data_1stPage['hits']
    print(n_jobs)
    if n_jobs//10 == 0:
        n_pages = n_jobs//10
    else:
        n_pages = n_jobs//10 + 1
    urls = [url_1stPage[:-1]+str(i*10) for i in range(n_pages)]

    # 'facets' stores statistics in 7 categories
    # for key,value in data_1stPage['facets'].items():
    # ...     print(key,'|',type(value))
    # ...
    # location_facet | <class 'list'>
    # business_category_facet | <class 'list'>
    # category_facet | <class 'list'>
    # schedule_type_id_facet | <class 'list'>
    # employee_class_facet | <class 'list'>
    # normalized_location_facet | <class 'list'>
    # job_function_id_facet | <class 'list'>
    # iterate through category_facet so each category has total jobs < 10000
    urls = []
    for cat in data_1stPage['facets']['category_facet']:
        name, number = list(cat.keys())[0], list(cat.values())[0]
        name = '-'.join(re.split('[^a-z]+', name.lower()))
        url_1stPage_cat = pre_url+'&category[]='+name+'&offset=0'
        data_1stPage_cat = requests.get(url_1stPage_cat).json()
        n_jobs = data_1stPage_cat['hits']
        if n_jobs//10 == 0:
            n_pages = n_jobs//10
        else:
            n_pages = n_jobs//10 + 1
        # somehow the corporate-operations category is missing from the webpage
        if name != 'corporate-operations':
            urls.extend([url_1stPage_cat[:-1]+str(i*10)
                         for i in range(n_pages)])

    # 'jobs' stores 10 job positions for each page
    # each job is a dictionary
    filen = '_'.join(query.split('+'))+'.csv'
    with open(filen, 'w') as csvfile:
        header_writer = csv.writer(csvfile)
        header_writer.writerow(data_1stPage['jobs'][0].keys())

    return(urls, filen)


def save_csv(urls, filen):
    with open(filen, 'a') as csvfile:
        jobs_writer = csv.writer(csvfile)
        for i, url in enumerate(urls):
            print('*'*60)
            print('Scraping page {p} out of {n_p}'.format(
                p=i+1, n_p=len(urls)))
            jobs = requests.get(url).json()
            print('-'*60)
            for j, job in enumerate(jobs['jobs']):
                print('Writing job {n} out of 10'.format(n=j+1))
                job['team'] = job['team']['label']
                jobs_writer.writerow(job.values())
            time.sleep(random.randint(1, 3))


query = 'aws'

urls, filen = get_urls_filename(query)
print(len(urls))
save_csv(urls, filen)
