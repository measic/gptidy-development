import os
import requests
from bs4 import BeautifulSoup

# 이미지를 가져오고 싶은, 웹툰의 특정 에피소드 주소를 지정해주세요.
ep_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=118&weekday=wed'

res = requests.get(ep_url)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.view_area img'):
    img_url = tag.get('src')  # ''
    if img_url:
        headers = {'Referer': ep_url}
        res = requests.get(img_url, headers=headers)
        img_data = res.content
        img_name = os.path.basename(img_url)  # url로부터 끝의 파일명을 뽑아냅니다.

        print('다운받는 중 ... ', img_name)

        img_path = '고수/' + img_name
        img_dirpath = os.path.dirname(img_path)
        if not os.path.exists(img_dirpath):
            os.makedirs(img_dirpath)

        with open(img_path, 'wb') as f:
            f.write(img_data)