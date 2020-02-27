from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

import pandas as pd
import numpy as np
import os

base_dir="D:\99.project\08.BMT\crawling"
file_name = "sport_663.xlsx"
xlxs_dir = os.path.join(base_dir, file_name)
result_title = []
result_content = []

base_url = "https://www.koreatimes.co.kr/www/sports/2020/02/663_{}.html"
#print(xlxs_dir)
for n in range(283959,283897,-1):
    print(n)
    url = base_url.format(n)
    print(url)
    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "html.parser")

    title_container = soup.find("div", {"class":"view_HD_div"})
    content_container = soup.find("div", {"id":"startts"})
    titles = title_container.find_all("div", {"class":"view_headline HD"})

    for title in titles:
        title = title.get_text()
        result_title.append(title)
        result_content.append(content_container.get_text())

data = {
            "제목" : result_title,
            "내용" : result_content
        }

df = pd.DataFrame(data, columns=['제목','내용'])
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')

writer.close()
