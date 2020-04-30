# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
j=595 #n장부터 시작
error=[] #에러 저장
for x in range(j-1, 645):
    i = 2746-x
    wraped_list=[]

    headers = {'User-Agent':'Chrome/66.0.3359.181'}
    url = 'https://cwy0675.tistory.com/'+str(i)
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    div_class = soup.find("div", {"class" : "article"})
    all_ps = div_class.find_all('p')

    for wrapper in all_ps:
        wraped_list.append(wrapper.text)\

    try:
        c_from = wraped_list.index("2016년 12월 최종수정.")
        c_to = len(wraped_list)
        wraped_list = [el.replace('\xa0', ' ') for el in wraped_list]
        fname = str(j) + ".txt"
        f = open(fname, 'w')
        for i in range(c_from+6, c_to):
            f.write(wraped_list[i])
            f.write("\n")
        f.close
        print(j, "장 끝")
        j = j + 1
    except ValueError:
        error.append(j)
        j=j+1
        pass
print("모든 작업 완료")
print(error)
