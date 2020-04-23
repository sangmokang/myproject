from selenium import webdriver
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.get('https://www.linkedin.com/')
driver.implicitly_wait(1.5)
driver.find_element_by_class_name('nav__button-secondary').click()

driver.implicitly_wait(5)

id = 'yahoo--@hanmail.net'
driver.implicitly_wait(3)
pw = 'rkdtjdah1#'

driver.implicitly_wait(3)

elem = driver.find_element_by_id("username")
driver.implicitly_wait(3)
elem.send_keys('yahoo--@hanmail.net')
elem = driver.find_element_by_id("password")
elem.send_keys('rkdtjdah1#')
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
driver.get('https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22kr%3A0%22%5D&keywords=python&origin=FACETED_SEARCH')

#여기까진 됨.
# driver.find_element_by_class_name('search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary').click()
# driver.find_element_by_css_selector( '.name actor-name').click()

# driver.execute_script("document.getElementsByName('username')[0].value = '{}'".format(id))
# driver.execute_script("document.getElementsByName('password')[0].value = '{}'".format(pw))

elements = driver.find_elements_by_tag_name('button')

for element in elements:
    className = element.get_attribute('class')
    print(className)
    if 'search-result__actions' in className:
        print ('aaaa: ',element)
        try:
            element.click()
            print('clicked')
        except:
            print('fail click')
            pass

search_result = soup.select('ul.search-results__list list-style-none')

for i in search_result:
    inner_html = driver.page_source
    inner_soup = BeautifulSoup(html, 'html.parser')
    driver.find_element_by_css_selector('.search-results__list list-style-none > button').click()
    print(i)




# driver.find_element_by_class_name('btn__primary--large from__button--floating').click()



# mailsender = soup.select('td.name a')
# for mail in mailsender:
#     print(mail['title'])


driver.close()
driver.quit()


