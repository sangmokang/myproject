#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import sys
import re
import configparser
import regex
from pyvirtualdisplay import Display
import sqlalchemy

config = configparser.ConfigParser()
config.read('../db.config')

from crawler_assist import crawling_term
from db_assist import Pg_database

# reload(sys)
# sys.setdefaultencoding('utf-8')


def remove_whitespace(text):
    clean_text = re.sub("[?|<|>|!|_|-|:|,|(|)|.]|\\|/", " ", text)
    return ''.join(clean_text.split())


def parsing_linkedin(rm_code, url, html, sql_con, sql_meta):

    db_help = Pg_database()

    personal_datum = {
        'rm_code' : 'null',
        'name' : 'null',
        'birth' : '1990',
        'age' : 0,
        'gender' : 'null',
        'mobile' : 'null',
        'email' : 'null',
        'address' : 'null',
        'job_keyword' : 'null',
        'job_title' : 'null',
        'educational_history' : 'null',
        'career_history' : 'null',
        'career_term' : 'null',
        'salary_requirement' : 'null',
        'working_area' : 'null'
    }

    education_datum = {
        'edu1_name' : '',
        'edu1_major' : '',
        'edu1_term' : '',
        'edu2_name' : '',
        'edu2_major' : '',
        'edu2_term' : '',
        'edu3_name' : '',
        'edu3_major' : '',
        'edu3_term' : ''
    }

    career_datum = {
        'career1_name' : '',
        'career1_duty' : '',
        'career1_work' : '',
        'career1_term' : '',
        'career1_salary' : '',
        'career2_name' : '',
        'career2_duty' : '',
        'career2_work' : '',
        'career2_term' : '',
        'career2_salary' : '',
        'career3_name' : '',
        'career3_duty' : '',
        'career3_work' : '',
        'career3_term' : '',
        'career3_salary' : '',
        'career4_name' : '',
        'career4_duty' : '',
        'career4_work' : '',
        'career4_term' : '',
        'career4_salary' : '',
        'career5_name' : '',
        'career5_duty' : '',
        'career5_work' : '',
        'career5_term' : '',
        'career5_salary' : '',
        'career6_name' : '',
        'career6_duty' : '',
        'career6_work' : '',
        'career6_term' : '',
        'career6_salary' : '',
        'career7_name' : '',
        'career7_duty' : '',
        'career7_work' : '',
        'career7_term' : '',
        'career7_salary' : '',
        'introduction' : 'intoduction',
        'career_description' : 'career_description'
        }

    parse_html = BeautifulSoup(html, 'html.parser')

    personal_datum['url'] = url
    # print 'url : ', url

    personal_datum['rm_code'] = rm_code
    # print 'rm_code : ', rm_code

    try:
        name = parse_html.find('h1', {'class':'pv-top-card-section__name inline t-24 t-black t-normal'}).get_text()
        personal_datum['name'] = name
        # print 'name : ', name
    except:
        pass

    try:
        job_keyword = parse_html.find('h2', {'class':'pv-top-card-section__headline mt1 t-18 t-black t-normal'}).get_text()
        personal_datum['job_keyword'] = job_keyword
        # print 'job_keyword : ', job_keyword
    except:
        pass

    try:
        introduction = parse_html.find('p', {'class':'pv-top-card-section__summary-text mt4 ember-view'}).get_text()
        career_datum['introduction'] = introduction
    except:
        pass
    # print 'introduction : ', career_datum['introduction']


    #educations parsing
    try:
        educations = parse_html.findAll('div', {'class':'pv-entity__summary-info pv-entity__summary-info--background-section'})
    except:
        educations = []
    # print 'educations : ' , educations

    index = 1
    for education in educations:
        e_name = "edu{}_name".format(index)
        e_major = "edu{}_major".format(index)
        e_term = "edu{}_term".format(index)
        try:
            edu_name = education.find('h3', {'class':'pv-entity__school-name t-16 t-black t-bold'}).get_text()
        except:
            edu_name = 'null'
        try:
            edu_major = education.find('p', {'class':'pv-entity__secondary-title pv-entity__fos pv-entity__secondary-title t-14 t-black--light t-normal'})
            edu_major = edu_major.find('span', {'class':'pv-entity__comma-item'}).get_text()
        except:
            edu_major = 'null'
        try:
            edu_terms = education.find('p', {'class':'pv-entity__dates t-14 t-black--light t-normal'})
            edu_term = ''
            for term in edu_terms.findAll('time'):
                #print term.get_text()
                edu_term = edu_term + '-' + term.get_text()
        except:
            edu_term = 'null'

        education_datum[e_name] = remove_whitespace(edu_name)
        education_datum[e_major] = remove_whitespace(edu_major)
        education_datum[e_term] = remove_whitespace(edu_term)


        index = index + 1

    try:
        careers = parse_html.findAll('div', {'class':'pv-entity__position-group-pager pv-profile-section__list-item ember-view'})
    except:
        careers = []
    # print 'careers : ' , careers

    index = 1
    for career in careers:
        c_name = 'career' + str(index) + '_name'
        c_duty = 'career' + str(index) + '_duty'
        c_work = 'career' + str(index) + '_work'
        c_term = 'career' + str(index) + '_term'
        c_salary = 'career' + str(index) + '_salary'

        try:
            career_name = career.find('span', {'class':'pv-entity__secondary-title'}).get_text()
        except:
            career_name = 'null'
        #career_duty = career.find('h4', {'class':'pv-entity__date-range t-14 t-black--light t-normal'}).get_text()
        try:
            career_works = career.find('div', {'class':'pv-entity__extra-details ember-view'})

            #print 'ccc : ', career_works
            career_work = ''
            for temp_work in career_works.findAll('span'):
                career_work = career_work + ' ' + temp_work.get_text()
        except:
            career_works = 'null'

        try:
            temp_terms = career.find('h4', {'class':'pv-entity__date-range t-14 t-black--light t-normal'}).findAll('span')
            career_term = ''
            for temp_term in temp_terms:
                career_term = career_term + '_' + temp_term.get_text()
        except:
            career_term = 'null'

        career_datum[c_name] = remove_whitespace(career_name)
        career_datum[c_duty] = remove_whitespace(career_work)
        career_datum[c_term] = remove_whitespace(career_term)

        # print '경력 : name:{}, duty:{}, term:{}'.format(
        #     remove_whitespace(career_name),
        #     remove_whitespace(career_work),
        #     remove_whitespace(career_term))
        index = index + 1

    parse_detail_html = BeautifulSoup(html, 'html.parser')
    try:
        phone = parse_detail_html.find('section', {'class':'pv-contact-info__contact-type ci-phone'})
        mobile = phone.find('span', {'class':'t-14 t-black t-normal'}).get_text()
    except:
        mobile = 'null'
    personal_datum['mobile'] = mobile
    # print 'phone : ', mobile

    try:
        email = parse_detail_html.find('section', {'class':'pv-contact-info__contact-type ci-email'})
        email = email.find('a', {'class':'pv-contact-info__contact-link t-14 t-black t-normal'}).get_text()
    except:
        email = 'null'
    personal_datum['email'] = email
    # print 'email : ', email

    #inserted_html = db_help.insert_html_data(personal_datum['rm_code'], str(html), 'null', sql_con, sql_meta)

    try:
        inserted_html = db_help.insert_html_data(personal_datum['rm_code'], str(html), 'null', sql_con, sql_meta)
        # print 'insert html database: ', personal_datum['rm_code']

    except:
        inserted_html = False
        # print 'fail to insert html database : ', personal_datum['rm_code']

    if inserted_html == True:
        try:
            inserted_ps = db_help.insert_ps_data(personal_datum, education_datum, career_datum)
            # print 'insert ps database: ', personal_datum['rm_code']
        except:
            pass
            # print 'fail to insert ps database(insert html)'
    else:
        pass
        # print 'fail to insert ps database because html: ', personal_datum['rm_code']