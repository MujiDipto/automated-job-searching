import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from termcolor import colored


# visit studenthub
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://studenthub.uq.edu.au/')

# click login as "Current Students and Staff"
button = driver.find_element_by_css_selector('body > div.main > div > div > div > div.sparse-body.auth-body > div > div.login-services > div > a')
button.click()
# driver.quit()


driver.implicitly_wait(5) # wait for the page to load
username = driver.find_element_by_name('username') # find the username field
password = driver.find_element_by_id("password") #find password field

# enter login credentials
username.send_keys("######")
password.send_keys("##########")
# click the login button
driver.find_element_by_name("submit").click()

# advanced search
driver.implicitly_wait(10) # wait for the page to load
more_search_options = driver.find_element_by_css_selector('#home-feature > div > form > div:nth-child(2) > div > div > ul > li > a > span')
more_search_options.click()

# set "Residency Requirements to All candidates including icleanternational students"
select = Select(driver.find_element_by_id('residency'))
select.select_by_value('All candidates considered including international students')

# click search
search = driver.find_element_by_css_selector('#home-feature > div > form > div:nth-child(3) > div > div > button')
search.click()

job_titles = []
company_names = []
job_info = []

containers = driver.find_elements_by_class_name("list-group-item")

for items in containers:
    titles = items.find_elements_by_tag_name('h4')
    companies = items.find_elements_by_tag_name('h5')
    info = driver.find_elements_by_class_name("job-list-info")
    for title, name, i in zip(titles, companies, info):
        job_titles.append(title)
        company_names.append(name)
        job_info.append(i)


for title, name, info in zip(job_titles, company_names, job_info ):
    text = colored(title.text, 'green', attrs=['reverse'])
    print(text)
    # print(colored(title.text, 'green'))
    print(colored(name.text, 'yellow'))
    print(info.text)
    print("\n")

driver.quit()
