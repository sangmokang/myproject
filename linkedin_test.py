from selenium import webdriver
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
import random
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.get('https://www.linkedin.com/')
driver.implicitly_wait(1.5)
driver.find_element_by_class_name('nav__button-secondary').click()


id = 'yahoo--@hanmail.net'
pw = 'rkdtjdah1#'

driver.implicitly_wait(3)

elem = driver.find_element_by_id("username")
time.sleep(2)
elem.send_keys(id)
elem = driver.find_element_by_id("password")
elem.send_keys(pw)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
keyword = 'es6'
page_num = '1'
url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B\"kr%3A0\"%5D&keywords={}&origin=SWITCH_SEARCH_VERTICAL&page={}".format(
                keyword,
                page_num)

driver.get(url)


# driver.find_element_by_class_name('search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary').click()
# driver.find_element_by_css_selector( '.name actor-name').click()

# driver.execute_script("document.getElementsByName('username')[0].value = '{}'".format(id))
# driver.execute_script("document.getElementsByName('password')[0].value = '{}'".format(pw))


# search_results = driver.find_element_by_xpath('//*[@class="search-results__list .list-style-none"]/div')
search_results =driver.find_element_by_class_name('search-results__list.list-style-none')

# print('search_results is', search_results)
search_results_lis = search_results.find_elements_by_tag_name("li")
print('search_results-lis', search_results_lis)

for search_results_li in search_results_lis:
    try:
        button = search_results_li.find_element_by_class_name("search-result__action-button")
    except NoSuchElementException:
        break

    print('button.is_enabled()', button.is_enabled())
    if button.is_enabled():
        button.click()
        message = '안녕하세요 저는 헤드헌터 Jeffery 라고 합니다. 1촌 신청 드립니다.'
        driver.find_element_by_xpath("""//*[@id="custom-message"]""").send_keys(message)
        driver.find_element_by_xpath(""" //button[@aria-label='1촌 신청 보내기'] """).click()
        time.sleep(random.randint(1, 3))

# elements = driver.find_elements_by_tag_name('button')
# friend_level = driver.find_element_by_xpath(""" //span[@class ='distance-badge separator ember-view'] """).text
# print(friend_level)
#
# #0425 1촌 신청을 했는지 확인하고 xpath 로 확인해서 신청 안보낸 애들만 클릭하하자. 17:21
#
#
# for element in elements:
#     className = element.get_attribute('class')
#     print('className is ', className)
#     message = '안녕하세요 저는 Tech 영역의 채용 일을 하고 있는 Jeffery 라고 합니다'
#     # print(className)
#     # if driver.find_element_by_link_text("2촌") in 1level_Friend:
#     '.artdeco-button:disabled'
#     if 'search-result__actions' in className:
#         if friend_level != '1촌':
#             try:
#                 element.click()
#                 print('clicked')
#                 driver.find_element_by_css_selector("#custom-message").send_keys(message)
#                 #여기까지는 됨
#                 # driver.implicitly_wait(5)
#                 driver.find_element_by_xpath(""" //button[@aria-label='1촌 신청 보내기'] """).click()
#                 time.sleep(random.randint(1, 3))
#
#             except Exception as e:
#                 print('fail click', e)
#                 pass
#
# search_result = soup.select('ul.search-results__list list-style-none')
#
# for i in search_result:
#     inner_html = driver.page_source
#     inner_soup = BeautifulSoup(html, 'html.parser')
#     driver.find_element_by_css_selector('.search-results__list list-style-none > button').click()
#     print(i)

# 문제.
# 1. 페이징처리
# 2. 1촌인 사람들 건너뛰어서 실행하기



#
# driver.close()
#

