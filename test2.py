from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

import pandas as pd
import numpy as np
import os

base_dir="D:\99.project\08.BMT\crawling"
file_name = "sport.xlsx"
xlxs_dir = os.path.join(base_dir, file_name)
result_title = []
result_content = []
content_url = []

base_url = "https://www.koreatimes.co.kr/www/section_600_{}.html"
#페이지로 이동하기
for n in range(1,100,+1):
    if n == 1:
        url = "https://www.koreatimes.co.kr/www/section_600.html"
    else:
        url = base_url.format(n) 
    html = urlopen(url)
    source = html.read()
    html.close()
    
    #제목과 url 가져오기, 제목 배열에 append하기
    soup = BeautifulSoup(source, "html.parser")
    title_container = soup.find("div", {"class":"all_section"})
    #print(title_container)
    titles = title_container.find_all("div",{"class":"list2_article_headline HD"})
    #print(titles)

    for title in titles:
        result_title.append(title.get_text())
        for curl in title.find_all('a'):
            print(curl['href'])
            content_url.append(curl['href'])

        print(content_url)
    print(result_title)
        
        
#가져온 url로 이동하여 내용 가져오기, 내용 배열에 append하기

##제목 내용을 엑셀에 넣기
