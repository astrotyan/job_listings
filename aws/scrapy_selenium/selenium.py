from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.amazon.jobs/en/search?base_query=aws&loc_query=')

driver.find_element_by_xpath('//*[@class="col-sm-6 job-count-info"]').text

driver.close()
