import requests
import json
import csv
import time
import random


def get_urls_filename(query):
    url_1stPage = 'https://www.amazon.jobs/en/search.json?base_query=' + query + \
        '&city=&country=&county=&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_function_id&latitude=&loc_group_id=&loc_query=&longitude=&offset=0&query_options=&radius=24km&region=&result_limit=10&sort=relevant&offset=0'

    # the response is in json format
    # .json() converts the json content to a dict
    data_1stPage = requests.get(url_1stPage).json()

    # data_1stPage.keys()
    # dict_keys(['error', 'hits', 'facets', 'jobs'])

    # hits stores the total number of rearch results
    n_jobs = data_1stPage['hits']

    # facets stores statistics in 7 categories
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

    #
    if n_jobs//10 == 0:
        n_pages = n_jobs//10
    else:
        n_pages = n_jobs//10 + 1

    urls = [url_1stPage[:-1]+str(i*10) for i in range(n_pages)]

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
            for j, job in enumerate(jobs['jobs']):
                print('Writing job {n} out of 10'.format(n=j+1))
                job['team'] = job['team']['label']
                jobs_writer.writerow(job.values())
            time.sleep(random.randint(1, 3))


query = 'aws'

urls, filen = get_urls_filename(query)
print(len(urls))
save_csv(urls[:3], filen)
