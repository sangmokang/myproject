from selenium import webdriver
import requests
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
import random
from selenium.common.exceptions import NoSuchElementException

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.linkedin                        # 'linkedin'라는 이름의 db를 만듭니다.


# 로그인
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

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

#강상모 프로필로 이동
driver.get('https://www.linkedin.com/in/michael-ji-hwan-yoon-50a61517b/')


# linkedin 강상모 이름선택
# linkedin_name = soup.select('.inline.t-24.t-black.t-normal.break-words') #뷰리풀솝 이용한 선택자
# linkedin_name = driver.find_element_by_xpath("""//*[contains(@class = "break-words")]""") #셀레니움 이용한 선택자 - 실패
linkedin_name = driver.find_element_by_css_selector('.inline.t-24.t-black.t-normal.break-words').text #그나마 뭐가 출력댐
friend_level = driver.find_element_by_css_selector('.dist-value').text
profile_title = driver.find_element_by_css_selector('.mt1.t-18.t-black.t-normal').text

#company 정보 for 문
companies = driver.find_elements_by_css_selector('.pv-entity__secondary-title.t-14.t-black.t-normal') #회사 목록의 리스트
career_periods = driver.find_elements_by_css_selector('pv-entity__date-range.t-14.t-black--light.t-normal') #회사별 재지긱간의 리스트
career_descriptions = driver.find_elements_by_css_selector('pv-entity__extra-details.t-14.t-black--light.ember-view') #회사별 했던 일들의 직무  기술
career_terms = driver.find_elements_by_css_selector('.t-14.t-black--light.t-normal')

for company in companies:
    print(company.text)

for career_period in career_periods:
    print(career_period.text)

for career_description in career_descriptions:
    print(career_description.text)

for career_term in career_terms:
    print(career_term.text)

career_datum = {'company' : company ,
                 'career_period': career_period,
                'career_description' : career_description,
                'career_term' : career_term,
                }

# i = 0

# for i in companies, career_period, career_description, career_term:
#
#     careers = {'companies' : companies.text ,
#          'career_period' : career_period.text,
#          'career_description' : career_description.text,
#          'career_term' : career_term.text,
#                }
#     print (careers)

# //*[@id="ember1216"]/div[2]/p[2]//*[@id="ember1216"]/div[2]/p[2]
linkedin_profile_pic = soup.select_one('.profile-photo-edit__edit-btn') #이건 사진
profile_summary = driver.find_element_by_css_selector('pv-about__summary-text.mt4.t-14.ember-view').text
job_title = driver.find_element_by_css_selector('h3.t-16.t-black.t-bold').text

# career_description = driver.find_elements_by_css_selector('.pv-entity__description.t-14.t-black.t-normal.inline-show-more-text.ember-view').text
# career_period = driver.find_elements_by_css_selector('.pv-entity__date-range.t-14.t-black--light.t-normal').text

# univ = driver.find_elements_by_css_selector('.pv-entity__school-name.t-16.t-black.t-bold').text
# univ_major = driver.find_elements_by_css_selector('.pv-entity__comma-item').text
# univ_term = driver.find_elements_by_css_selector('.pv-entity__dates.t-14.t-black--light .t-normal').text
# skill = driver.find_elements_by_css_selector('.pv-skill-category-entity__name-text.t-16.t-black.t-bold').text
# email = driver.find_element_by_css_selector('.inline.t-24.t-black.t-normal.break-words').text #이건 팝업 띄워야 해서 ㅜㅜ
# profile_html =
profile_url = driver.current_url
profile_html = html


print(linkedin_name, friend_level, profile_title, companies, profile_summary, job_title, career_terms, )
#
# #오ㅏ 드디ㅓ ㅇ....
#
doc = {
    'linkedin_name': linkedin_name,
    'company' : company,
    'career_datum' : career_datum,
    'profile_url' : profile_url,
    'friend_level' : friend_level,
    'profile_title': profile_title,
    'profile_summary' : profile_summary,
    'job_title' : job_title,
    'career_terms' : career_term,
    'profile_url': profile_url,
    'profile_html' : html,
    'linkedin_profile_pic' : linkedin_profile_pic,
}
#
# db.linkedinprofile.insert_one(doc)

# # movies (tr들) 의 반복문을 돌리기
# rank = 1
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#         print(rank,title,star)
#         rank += 1



# current_url = driver.current_url
# url = current_url
#
# driver.get(url)
##url 관련해서 자바스크립트로 현재 url 을 가져와야 하고 그 url 을 py 에 전달하여
# window.location.href - 현재 페이지의 href (URL) 반환








