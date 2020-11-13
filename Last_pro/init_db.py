import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


def get_urls():
    # 타겟 URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&tg=0&date=20201106', headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    movies = soup.select('#old_content > table > tbody > tr')

    urls = []
    for movie in movies:
        a = movie.select_one('td.title > div > a')
        if a is not None :
            base_url = 'https://movie.naver.com/'
            url = base_url + a['href']
            urls.append(url)

    return urls


def insert_movie(i,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a > img')['src']
    one_line_sum = soup.select_one('#content > div.article > div.section_group.section_group_frst> div>div>div > h5')
    # content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div
    summary = soup.select_one('#content > div.article > div.section_group.section_group_frst > div>div> div.story_area > p').text
    # content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > h5
    one_line =""
    if one_line_sum is not None:
        one_line = one_line_sum.name
    doc = {
        'name': name,
        'img_url': img_url,
        'one_line': one_line,
        'summary': summary,
        'url': url,
        'id':i
    }

    db.moviesmin.insert_one(doc)
    print('완료!', name)


def insert_all():
        db.moviesmin.drop()  # mystar 콜렉션을 모두 지워줍니다.
        urls = get_urls()
        i =1
        for url in urls:
            insert_movie(i, url)
            i =i+1



    ### 실행하기
insert_all()


    # movies (tr들) 의 반복문을 돌리기
#    for movie in movies:
        # movie 안에 a 가 있으면,
#        a_tag = movie.select_one('td.title > div > a')
#        if a_tag is not None:
            # a의 text를 찍어본다.
#            rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
#            title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
#            star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
#            print(rank, title, star)


