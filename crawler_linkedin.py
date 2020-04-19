from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import sys
import re
import ConfigParser
import regex
from pyvirtualdisplay import Display
from parsing_linkedin import parsing_linkedin
import sqlalchemy

config = ConfigParser.ConfigParser()
config.read('./db.config')

from crawler_assist import crawling_term
from db_assist import Pg_database

reload(sys)
sys.setdefaultencoding('utf-8')

def crawling_linkedin(keywords, area, age, career, page_threshold, sql_con, sql_meta):

    db_help = Pg_database()

    path = config.get('FILE_PATH','chromedriver')
    driver = webdriver.Chrome(path)

    base_url = 'https://www.linkedin.com/'
    url = 'https://www.linkedin.com/'
    driver.get(url)

    crawling_term(100)
    #driver.find_element_by_css_selector('#loginForm > div > div.head.clear > ul > li:nth-child(2) > label > span').click()
    driver.find_element_by_name('session_key').send_keys('krama9181@gmail.com')
    crawling_term(100)
    driver.find_element_by_name('session_password').send_keys('junseok11!')
    crawling_term(100)
    driver.find_element_by_xpath('//*[@id="login-submit"]').click()
    crawling_term(100)

    for keyword in keywords.split('|'):
        for page_num in range(1, page_threshold+1):
            cr_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B\"kr%3A0\"%5D&keywords={}&origin=SWITCH_SEARCH_VERTICAL&page={}".format(
                keyword,
                page_num)

            driver.get(cr_url)

            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.PAGE_DOWN)
            crawling_term(100)
            body.send_keys(Keys.PAGE_DOWN)
            crawling_term(100)
            body.send_keys(Keys.PAGE_DOWN)
            crawling_term(100)

            main_html = driver.page_source
            soup = BeautifulSoup(main_html, 'html.parser')

            resume_lists = soup.find_all('li', {'class':'search-result search-result__occluded-item ember-view'})
            crawling_term(30)

            for resume_list in resume_lists:
                print 'resume_list : ', resume_list.find('a').get('href')

            #resume_lists = ['/in/sungeuns2/']

            for resume_list in resume_lists:
                resume_list = resume_list.find('a').get('href')

                resume_list = '/in/pinkwink/'

                resume_url = "https://www.linkedin.com{}".format(resume_list)
                contact_url = "https://www.linkedin.com{}detail/contact-info".format(resume_list)

                print 'resume_url : ', resume_url
                print 'contact_url : ', contact_url

                crawling_term(50)
                driver.get(resume_url)
                body = driver.find_element_by_tag_name('body')
                op_html = driver.page_source
                op_soup = BeautifulSoup(op_html, 'html.parser')
                crawling_term(100)
                body.send_keys(Keys.PAGE_DOWN)
                crawling_term(100)
                body.send_keys(Keys.PAGE_DOWN)
                crawling_term(100)
                body.send_keys(Keys.PAGE_DOWN)
                crawling_term(100)
                body.send_keys(Keys.PAGE_DOWN)
                crawling_term(100)

                elements = driver.find_elements_by_tag_name('button')
                for element in elements:
                    className = element.get_attribute('class')
                    #print(className)
                    if className == 'pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar':
                        #print 'aaaa: ',element
                        try:
                            element.click()
                            print 'clicked'
                        except:
                            print 'fail click'
                            pass
                """
                elements = driver.find_element_by_class_name('pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar').click()
                for e in elements:
                    print 'e : ', e
                    e.click()
                crawling_term(100)
                """

                crawling_term(100)
                #rm_code = 'linkedin_' + resume_list.find('a').get('href')
                rm_code = 'linkedin_' + resume_list

                driver.get(contact_url)
                contact_html = driver.page_source
                contact_soup = BeautifulSoup(contact_html, 'html.parser')

                parsing_linkedin(rm_code, contact_url, contact_html, sql_con, sql_meta)

                crawling_term(100)


    drvier.close()
    driver.quit()
    return True

if __name__ == '__main__':
    #keywords = ['machine learning', 'deep learning', 'ML', 'DL', 'tensorflow', 'pytorch', 'spark']
    #for keyword in keywords:
    crawling_linkedin('python','b','c','d',2)

