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

mailrecipient = soup.select('td.name span a')
mailtitle = soup.select('td.title a')
sendtime = soup.select('td.date a')
readtime = soup.select('td.date a')
# mailbody = soup.select('td.date a')
sendmails = soup.select('#tdMailList > .listbox tr td.title .in a')

print(sendmails[1].text.strip())

i = 0
for i in sendmails:
    # eachmail = driver.find_elements_by_css_selector('td.title .in a')
    # i.click()
    # # i += 1
    print(i.text.strip())

#제목 출력해보기
# for i in sendmails:
#     # i.click()
#     print(i.text)
#done

#제목을 각각 클릭해보기

i = 0
a = []
eachmail = []

# for eachmail in sendmails:
#     eachmail = driver.find_elements_by_css_selector('td.title .in a')
#     print(eachmail)
# i += 1
    # print()

# eachmail = []
# while True:
#     eachmail = driver.sendmails.find_elements_by_css_selector('td.title .in a')
#     print(eachmail)
#     # print(eachmail[i].text)

#
# for i in sendmails:
#     eachmail = driver.find_element_by_css_selector('td.title .in a')
#     print(eachmail)
    # i = i + 1
    # driver.execute_script("window.history.go(-1)")
    # print(sendmail.text)
    # [].click()

# a = []
# order = 0
# for sendmail in sendmails:
#
#     # title_tag = driver.find_element_by_id(i.get('id'))
#     title_tag = driver.find_elements_by_css_selector('.title .in a')
#     # sendmail.title_tag.click()
#     # print(title_tag)
#     sendmail.click()
#     # a.append(title_tag.text)
#     # print(a)
#     # title_tag.click()
#
#
#     driver.execute_script("window.history.go(-1)")
#     order += 1



    # inner_html = driver.page_source
    # inner_soup = BeautifulSoup(html, 'html.parser')
    # # print(inner_soup)
    # driver.switch_to.frame('ifMailContent')
    # # inner_iframe_html = driver.page_source
    # # inner_iframe_soup = BeautifulSoup(html, 'html.parser')
    # mailbody = soup.select_one('#divcontent #FrameTable tobody tr td div p')
    # # switch_to_default_content()
    # print(mailbody)


    # print(i.select_one('.title .in'))
    # driver.find_element(i.select_one('.title .in')).click()


    # mailreceipts = i.select_one('td.name a').text.strip()
    # mailtitle = i.select_one('td.title a').text.strip()
    # sendtime = i.select_one('td.date').text.strip()
    # readtime = i.select_one('tbody td:nth-child(10)').text.strip()
    # maillist = {"mailreceipts": mailreceipts,
    #             "mailtitle": mailtitle,
    #             "sendtime": sendtime,
    #             "readtime": readtime,
    #             "mailbody": mailbody,
    #             }

    # print(i)
    # print(maillist)

#
#
# page = 0
# pages = []
# # pages = soup.select('.paginate a')
# pages = soup.find_all('div', {'id': 'divMainPaging'})
# print(pages)
#
# for i in pages:
#     print(i)
#     i.click


# for i in pages:

    # page_tags = "//*[@id=\"divMainPaging\"]/a["
    # page_tags += i
    # page_tags += "]"
    # i = i + 1
    # print(page_tags)
    # driver.find_element_by_xpath(page_tags).click()

    # page_tags = soup.find_element_by_xpath(""" //*[@id ="divMainPaging"]/ a[] """)

# print(page_tags)
# pages = soup.find_element_by_xpath(""" //*[@class = 'paginate' """)
# page_tags = pages.find_element_by_xpath(""" //*[@id ="divMainPaging"]/ a[{}] """).format(i)

#
# for page in pages:
#     try:
#         page.find_element_by_xpath(""" //*[@id ="divMainPaging"]/ a[{}] """).format(i)
#         page.click()
#         print(page)
#
#     except:
#         pass
#
# i = 1
#
# for i in pages:
#     page_tags = soup.find_element_by_queryselector('a')
#     # page_tags = driver.find_element_by_xpath(""" //*[@id ="divMainPaging"]/ a[" + i + "] """).format(i)
#     print(page_tags)
#     page_tags.click()
#     i = i + 1




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
driver.quit()

