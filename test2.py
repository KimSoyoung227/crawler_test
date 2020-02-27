from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

import pandas as pd
import numpy as np
import os

base_url = "https://www.koreatimes.co.kr"   # 기본 사이트 url
base_dir="D:\99.project\08.BMT\crawling"    # 생성될 엑셀파일 경로
file_name = "sports.xlsx"                   # 생성될 엑셀파일명
xlxs_dir = os.path.join(base_dir, file_name)
result_title = []
result_content = []
contents_url = []


# 페이지로 이동하기
for n in range(1,50,+1):
    print(n);
    if n == 1:
        url = base_url + "/www/sublist_600.html"
    else:
        url = base_url + "/www/sublist_600_{}.html".format(n)
    html = urlopen(url)
    source = html.read()
    html.close()
    
    # 제목과 url 가져오기, 제목 배열에 append하기
    soup = BeautifulSoup(source, "html.parser")
    title_container = soup.find("div", {"class":"all_section"})
    titles = title_container.find_all("div",{"class":"list_article_headline HD"})
    # print(titles)
    
    for title in titles:
        result_title.append(title.get_text())
        
        # 가져온 url로 이동하여 내용 가져오기, 내용 배열에 append하기
        content_url = base_url + title.find('a')['href']
        html2 = urlopen(content_url)
        source2 = html2.read()
        html2.close()

        soup2 = BeautifulSoup(source2, "html.parser")
        content_container = soup2.find("div", {"id":"startts"})
        result_content.append(content_container.text)
        # print(len(content_container))
    
# 제목,내용을 엑셀에 넣기
data = {"제목" : result_title, "내용" : result_content}
df = pd.DataFrame(data, columns=['제목','내용'])
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')

writer.close()
