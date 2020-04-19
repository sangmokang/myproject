from selenium import webdriver
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.linkedin.com/')
driver.implicitly_wait(1.5)
driver.find_element_by_class_name('nav__button-secondary').click()

id = 'yahoo--@hanmail.net'
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


# driver.find_element_by_class_name('search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary').click()
driver.find_element_by_css_selector( '.name actor-name').click()

# driver.execute_script("document.getElementsByName('username')[0].value = '{}'".format(id))
# driver.execute_script("document.getElementsByName('password')[0].value = '{}'".format(pw))


driver.find_element_by_class_name('btn__primary--large from__button--floating').click()
driver.find_element_by_class_name('fold').click()
driver.find_element_by_id('mbox_name_b1').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print(soup.text)



mailtitle = soup.select('td.title a')
for mail in mailtitle:
    print(mail['title'])
    a = mail['title'].search("제안")
    print(a)

# mailsender = soup.select('td.name a')
# for mail in mailsender:
#     print(mail['title'])


driver.close()

