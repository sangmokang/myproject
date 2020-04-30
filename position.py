from selenium import webdriver
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


db.position.insert_one({'':'',
'open_date':'2020.04.28 23:08',
'close_date':'2020.04.28 23:09',
'client':'스타일쉐어',
'position_title':'Python 개발 팀장',
'job_description':'긴문자와 따옴표  쉼표갇 들어 있는 JD',
'job_category':'PM',
'position_level':'manager',
'age_range':'30~45',
'consultant':'Tim Sangmo, Kang',
'co_worker':'Jeffery',
'position_status':'Alive - Holding - Close',
'location':'Seoul, Gangnam',
'salary_range':'5000~12000',
'sex':'-',
'expected_bill_amount':'10000',
'hiring_volume':'3',
'open_assign':'Open',
                   })
