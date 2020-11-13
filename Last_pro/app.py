from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/move', methods=['GET'])
def move_page():
    #1. btn 에서 데이터 갖고 오기.
    #장고랑 유튜브 사용할거임.
    test='test'
    return render_template('detail_v1.html',data=test)


@app.route('/api/list', methods=['GET'])
def show_movies():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    movies = list(db.moviesmin.find({}, {'_id': 0}))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result':'success', 'movies_list':movies})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
