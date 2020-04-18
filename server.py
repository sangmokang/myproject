from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles = list(db.articles.find({},{"_id":0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'articles' : articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
        article_url = request.form['article_url']
        comment = request.form['comment']
        # 2. meta tag를 스크래핑하기
        # url = 'https://platum.kr/archives/120958'


        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(article_url, headers=headers)

        # request --> ajax 를 요청
        # BeautifulSoup --> 제어

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        data = {
            'url': article_url,
            'image':og_image.get('content'),
            'title':og_title.get('content'),
            'description': og_description('content'),
            'comment':comment
        }

        # 3. mongoDB에 데이터 넣기
        db.articles.insert_one(data)
        return jsonify({'result': 'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

# 링크드인의 선택자를 파싱해온다.
# 몽고디비로 json 형태로 서버에 넘긴다 .
# 1. chrome webdriver 를 통하여 로그인
# 2.