from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

driver.get('https://office.hiworks.com/careersherpa.co.kr/')

id = 'rmrm'
pw = 'sang9star!!'

driver.execute_script("document.getElementsByName('office_id')[0].value = '{}'".format(id))
driver.execute_script("document.getElementsByName('office_passwd')[0].value = '{}'".format(pw))
driver.find_element_by_class_name('int_jogin').click()
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

