from flask import Flask, render_template, jsonify
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.linkedin                        # 'linkedin'라는 이름의 db를 만듭니다.

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/position')
def position():
   return render_template('position.html')

@app.route('/api/resume', methods=['GET'])
def show_resume():
		# 1. DB에서 resume 정보 모두 가져오기
    resume_list = list(db.linkedinprofile.find({},{'_id':0}))
    # print(resume_list)
		# 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'resume_list': resume_list})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)