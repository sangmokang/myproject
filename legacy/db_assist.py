#-*- coding: utf-8 -*-

import re
import json
import psycopg2
import operator
from datetime import datetime
import configparser
import sqlalchemy

config = configparser.ConfigParser()
config.read('./db.config')

sf = open(config.get('FILE_PATH','top_school'))
school_list = [line.rstrip() for line in sf.readlines()]
sf.close()


#school_list = ['서울대학교', '연세대학교', '고려대학교']

class Pg_database:
    def __init__(self):
        self.host = config.get('DB_CONFIG','host')
        self.port = config.get('DB_CONFIG','port')
        self.dbname = config.get('DB_CONFIG','db')
        self.user = config.get('DB_CONFIG','user')
        self.password = config.get('DB_CONFIG','passwd')
        self.rm_table = config.get('DB_CONFIG','rm_table')
        self.memo_table = config.get('DB_CONFIG','memo_table')
        self.accounts_table = config.get('DB_CONFIG','accounts_table')
        self.mail_table = config.get('DB_CONFIG','mail_table')
        self.sms_table = config.get('DB_CONFIG','sms_table')
        self.position_table = config.get('DB_CONFIG','position_table')
        self.html_table = config.get('DB_CONFIG','html_table')
        self.career_table = config.get('DB_CONFIG','career_table')
        self.education_table = config.get('DB_CONFIG','education_table')


    def update_html_data(self, rm_code, new_html, new_detail_html, con, meta):
        connection = con.connect()
        table = sqlalchemy.Table(self.html_table, meta, autoload=True, autoload_with=con)

        query = sqlalchemy.update(table).values(html = new_html, detail_html = new_detail_html)
        query = query.where(table.c.rm_code == rm_code)
        connection.execute(query)

        return True


    @staticmethod
    def cut_data_length(input_data, length):
        if len(input_data) > length:
            return input_data[:length]
        else:
            return input_data


    @staticmethod
    def date_check(date_value):
        #print 'before date_value : ', date_value
        if date_value.find('년'):
            #print 'after date_value : ', date_value
            return '9999-01-01'
        else:
            return date_value


    @staticmethod
    def salary_check(salary):
        #print 'before date_value : ', date_value
        if salary.find('만원'):
            #print 'after date_value : ', date_value
            return salary
        else:
            return 'null'


    @staticmethod
    def integer_check(text):
        return int(filter(str.isdigit,str(text)))


    @staticmethod
    def clean_string(text):
        return re.sub("[?|<|>|!|_|-|:|,|(|)|.]|\\|/", " ", text)


    @staticmethod
    def age_calculate_birth(birth_year):
        year_now = int(datetime.now().strftime('%Y'))
        birth = int(birth_year)
        return year_now - birth + 1


    @staticmethod
    def check_data_available(ps_db_data):
        clean_ps_db={}
        clean_ps_db['rm_code'] = ps_db_data['rm_code']
        clean_ps_db['name'] = Pg_database.cut_data_length(ps_db_data['name'], 18)
        clean_ps_db['birth'] =  Pg_database.integer_check(ps_db_data['birth'])
        clean_ps_db['gender'] = Pg_database.cut_data_length(ps_db_data['gender'], 2)
        clean_ps_db['mobile'] = Pg_database.cut_data_length(ps_db_data['mobile'], 18)
        clean_ps_db['email'] = Pg_database.cut_data_length(ps_db_data['email'], 28)
        clean_ps_db['address'] = Pg_database.cut_data_length(ps_db_data['address'], 90)
        clean_ps_db['job_keyword'] = Pg_database.cut_data_length(ps_db_data['job_keyword'], 100)
        clean_ps_db['job_title'] = Pg_database.cut_data_length(ps_db_data['job_title'], 20)
        clean_ps_db['educational_history'] = Pg_database.cut_data_length(ps_db_data['educational_history'], 18)
        clean_ps_db['career_history'] = Pg_database.cut_data_length(ps_db_data['career_history'], 18)
        clean_ps_db['career_term'] = Pg_database.cut_data_length(ps_db_data['career_term'], 18)
        clean_ps_db['salary_requirement'] = Pg_database.cut_data_length(ps_db_data['salary_requirement'], 20)
        clean_ps_db['working_area'] = Pg_database.cut_data_length(ps_db_data['working_area'], 18)

        try:
            clean_ps_db['url'] = ps_db_data['url']
        except:
            clean_ps_db['url'] = 'null'
        #for key, value in clean_ps_db.items():
        #    print key , ' : ', value

        return clean_ps_db


    @staticmethod
    def remove_tag(text):
        try:
            #print 'type : ', type(text)
            cleanr =re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', text)
            return cleantext

        except:
            #print text
            print('fail to remove tag')


    def insert_ps_data(self, ps_db_data, education_datum, career_datum):
        conn = psycopg2.connect(
            host = self.host,
            dbname = self.dbname,
            user = self.user,
            password = self.password)

        ps_db_data = self.check_data_available(ps_db_data)
        cur = conn.cursor()

        query = "INSERT INTO " + self.rm_table + \
            " (rm_code, name, birth, gender, mobile, email, address, job_keyword, job_title, educational_history, career_history, career_term, salary_requirement, modified_date, url)" \
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        try:
            cur.execute(query, (
                ps_db_data['rm_code'],
                ps_db_data['name'],
                ps_db_data['birth'],
                ps_db_data['gender'],
                ps_db_data['mobile'],
                ps_db_data['email'],
                ps_db_data['address'],
                ps_db_data['job_keyword'],
                ps_db_data['job_title'],
                ps_db_data['educational_history'],
                ps_db_data['career_history'],
                ps_db_data['career_term'],
                ps_db_data['salary_requirement'],
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                ps_db_data['url']))
                #ps_db_data['working_area']))

            query = "INSERT INTO " + self.education_table + \
                " (rm_code, edu1_term, edu1_major, edu1_name, edu2_term, edu2_major, edu2_name, edu3_term, edu3_major, edu3_name)" \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

            cur.execute(query, (
                ps_db_data['rm_code'],
                education_datum['edu1_term'],
                education_datum['edu1_major'],
                education_datum['edu1_name'],
                education_datum['edu2_term'],
                education_datum['edu2_major'],
                education_datum['edu2_name'],
                education_datum['edu3_term'],
                education_datum['edu3_major'],
                education_datum['edu3_name']))

            query = "INSERT INTO " + self.career_table + \
                " (rm_code, introduction, career_description," \
                " career1_name, career1_duty, career1_work, career1_term, career1_salary," \
                " career2_name, career2_duty, career2_work, career2_term, career2_salary," \
                " career3_name, career3_duty, career3_work, career3_term, career3_salary," \
                " career4_name, career4_duty, career4_work, career4_term, career4_salary," \
                " career5_name, career5_duty, career5_work, career5_term, career5_salary," \
                " career6_name, career6_duty, career6_work, career6_term, career6_salary," \
                " career7_name, career7_duty, career7_work, career7_term, career7_salary)" \
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                " %s, %s, %s, %s, %s, %s, %s, %s);"

            cur.execute(query, (
                ps_db_data['rm_code'], career_datum['introduction'], career_datum['career_description'],
                career_datum['career1_name'],
                career_datum['career1_duty'],
                career_datum['career1_work'],
                career_datum['career1_term'],
                career_datum['career1_salary'],
                career_datum['career2_name'],
                career_datum['career2_duty'],
                career_datum['career2_work'],
                career_datum['career2_term'],
                career_datum['career2_salary'],
                career_datum['career3_name'],
                career_datum['career3_duty'],
                career_datum['career3_work'],
                career_datum['career3_term'],
                career_datum['career3_salary'],
                career_datum['career4_name'],
                career_datum['career4_duty'],
                career_datum['career4_work'],
                career_datum['career4_term'],
                career_datum['career4_salary'],
                career_datum['career5_name'],
                career_datum['career5_duty'],
                career_datum['career5_work'],
                career_datum['career5_term'],
                career_datum['career5_salary'],
                career_datum['career6_name'],
                career_datum['career6_duty'],
                career_datum['career6_work'],
                career_datum['career6_term'],
                career_datum['career6_salary'],
                career_datum['career7_name'],
                career_datum['career7_duty'],
                career_datum['career7_work'],
                career_datum['career7_term'],
                career_datum['career7_salary']
                ))

        except psycopg2 as IntegrityError:
            conn.rollback()
            cur.close()
            conn.close()
            return False

        else:
            conn.commit()
            cur.close()
            conn.close()
            return True


    def insert_html_data(self, rm_code, html, detail_html, con, meta):
         connection = con.connect()
         html_table = sqlalchemy.Table(self.html_table, meta, autoload=True, autoload_with=con)

         i = sqlalchemy.insert(html_table)
         i = i.values(
             {"rm_code": rm_code,
              "html": html,
              "detail_html":detail_html})
         connection.execute(i)

         return True


    def load_html_data(self, rm_code, con, meta):
         connection = con.connect()
         html_table = sqlalchemy.Table(self.html_table, meta, autoload=True, autoload_with=con)

         query = sqlalchemy.select([html_table])
         ResultProxy = connection.execute(query)
         ResultSet = ResultProxy.fetchall()

         return ResultSet