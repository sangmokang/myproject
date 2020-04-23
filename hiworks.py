from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.hiworks                      # 'dbsparta'라는 이름의 db를 만듭니다.

maximum = 0
page = 1

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


page = 1
pages = soup.select('.paginate')
# print(pages)

for i in pages:
    page_tag = soup.find_element_by_tag_name('a')
    print(page_tag)

    page_tag.click()




order = 0

for i in sendmails:
    title_tag = driver.find_element_by_id(i.get('id'))
    title_tag.click()

    inner_html = driver.page_source
    inner_soup = BeautifulSoup(html, 'html.parser')
    # print(inner_soup)
    driver.switch_to.frame('ifMailContent')
    # inner_iframe_html = driver.page_source
    # inner_iframe_soup = BeautifulSoup(html, 'html.parser')
    mailbody = soup.select_one('#divcontent #FrameTable tobody tr td div p')
    # switch_to_default_content()
    print(mailbody)

    driver.execute_script("window.history.go(-1)")
    order += 1
    # print(i.select_one('.title .in'))
    # driver.find_element(i.select_one('.title .in')).click()


    mailreceipts = i.select_one('td.name a').text.strip()
    mailtitle = i.select_one('td.title a').text.strip()
    sendtime = i.select_one('td.date').text.strip()
    readtime = i.select_one('tbody td:nth-child(10)').text.strip()
    maillist = {"mailreceipts": mailreceipts,
                "mailtitle": mailtitle,
                "sendtime": sendtime,
                "readtime": readtime,
                "mailbody": mailbody,
                }

    # print(i)
    print(maillist)


#paging 처리
#메일을 돌면서 메일 내용 가져오기
#
# pages = soup.select('.pagenate .paging_numbers')
# print(pages)
# for i in pages:
#
#     db.maillist.insert_one(maillist)
#
# while 1:
#     page_list = soup.findAll("a", {"class": "NP=r:" + str(page)})
#     if not page_list:
#         maximum = page - 1
#         break
#     page = page + 1
# print("총 " + str(maximum) + " 개의 페이지가 확인 됬습니다.")

    # db.users.insert_one({'name': 'bobby', 'age': 21})

#     doc = {
#         'mailreceipt' : a,
#         'mailtitle' : b,
#         'sendtime' : c,
#     }

#
# len(maillist), maillist




# mailsender = soup.select('td.name a')
# for mail in mailsender:
#     print(mail['title'])


driver.close()
self.browser.close()

