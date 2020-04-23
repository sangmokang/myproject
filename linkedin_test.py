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

driver.implicitly_wait(3)

id = 'yahoo--@hanmail.net'
driver.implicitly_wait(3)
pw = 'rkdtjdah1#'

driver.implicitly_wait(3)

elem = driver.find_element_by_id("username")
driver.implicitly_wait(20)
elem.send_keys(id)
elem = driver.find_element_by_id("password")
elem.send_keys(pw)
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
    message = '안녕하세요 저는 Tech 영역의 채용 일을 하고 있는 Jeffery 라고 합니다'
    # print(className)
    if 'search-result__actions' in className:
        # print ('aaaa: ',element)
        try:
            element.click()
            print('clicked')
            driver.find_element_by_css_selector("#custom-message").send_keys(message)
            driver.implicitly_wait(5)
            driver.find_element_by_xpath(""" //button[@aria-label='1촌 신청 보내기'] """).click()
            time.sleep(random.randint(1, 3))
            #
            # if 'artdeco-button--primary' in className:
            #     element.click()
            # # element.send_keys(keys.RETURN)
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


# driver.close()


