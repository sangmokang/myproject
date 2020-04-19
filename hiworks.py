from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.hiworks                      # 'dbsparta'라는 이름의 db를 만듭니다.

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

mailreceipts = soup.select('td.name a')
# mailtitle = soup.select('td.title a')
# sendtime = soup.select('td.date a')
# readtime = soup.select('td.date a')
# maillist = [mailreceipt]
sendmails = soup.select('#tdMailList > .listbox tr')
# print(sendmails)


for i in sendmails:
    # print(i)
    mailreceipts = soup.select_one('td.name a').text.strip()
    mailtitle = soup.select_one('td.title a').text.strip()
    # sendtime = soup.select_one('td.date').text.strip()
    # readtime = soup.select_one('td.date a').text.strip()
    maillist = {"mailreceipts": mailreceipts,
                "mailtitle": mailtitle,
                }

    print(maillist)
#     doc = {
#         'mailreceipt' : a,
#         'mailtitle' : b,
#         'sendtime' : c,
#     }
#     db.maillist.insert_one(doc)
#
# len(maillist), maillist




# mailsender = soup.select('td.name a')
# for mail in mailsender:
#     print(mail['title'])


driver.close()
self.browser.close()

