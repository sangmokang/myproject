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

companies = ["a", "b", "c"]
career_period_list = ["d", "e", "f"]

last = len(companies)-1
item_range = range(0, last) # 3

empty_list = []
if len(companies) == len(career_period_list):

for i in item_range:
    # 0, 1, 2
    company = companies[i]
    career_period = career_period_list[i]
    value = {'compnay': company, 'career_period': career_period}
    empty_list.append(value)

final = {
    'linkedin_name': 'sangmokang',
    'friend_level' : '1촌',
    'company_datum': empty_list
}


sub_value_a = {'company': 'Hokhmah Consulting',
                  'career_period':'2014.01 ~ 2016.12',
                  'career_description' : '헤드헌팅 경력 Loren ipsum',
                  'career_term' : '3년',
                  }
sub_value_b = {'company': 'Guiness Consulting',
                  'career_period':'2011.01 ~ 2013.12',
                  'career_description' : '제조업 관련 서치',
                  'career_term' : '2년' ,
                  }
test_key = [sub_value_a, sub_value_b]
doc = {
    'linkedin_name': 'sangmokang',
    'friend_level' : '1촌',
    'profile_title' : 'Java Developer, Clean Coder',
    'current_company' : 'careersherpa',
    'linkedin_profile_pic' : '',
    'profile_summary' : 'Tech sector Headhunter',
    'job_title' : 'Sector Chief',
    'profile_url' : 'https://www.linkedin.com/in/coffeenlunch/',
    'profile_html': '',
    'company_datum': empty_list,
    'edu_datum' : [{'univ': 'Myungji Univ',
                  'univ_major':'Business',
                  'univ_period' : '1998 ~ 2004',
                  },
                  ],
    }

db.linkedinprofile.insert_one(doc)


