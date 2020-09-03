from bs4 import BeautifulSoup
import requests
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
import re

get_url_info = requests.post('https://dic.nicovideo.jp/b/a/%E5%8D%AF%E6%9C%88%E3%82%B3%E3%82%A6/1-')
soup = BeautifulSoup(get_url_info.text, 'html.parser')

elems_page = soup.select('.st-pg_contents')
page_no = re.findall('[0-9]+', elems_page[0].text)
last = int(page_no[len(page_no) - 1])

print(last)

"""
get_url_info = requests.post('https://dic.nicovideo.jp/b/a/%E5%8D%AF%E6%9C%88%E3%82%B3%E3%82%A6/1-')
soup = BeautifulSoup(get_url_info.text, 'html.parser')

elems_no = soup.select('.st-bbs_resNo')
elems_info = soup.select('.st-bbs_resInfo')
elems_body = soup.select('.st-bbs_resbody')
with open('test.txt', 'w'):
    pass
m = ""

for i in range(len(elems_no)):
    with open('test.txt', mode='a',encoding='utf_8') as f:
        f.write(elems_no[i].text.replace(" ","").replace("\n",""))
        f.write("\n")
        f.write(elems_info[i].text.replace(" ","").replace("\n",""))
        f.write("\n")
        f.write(elems_body[i].text.replace(" ","").replace("\n",""))
        f.write("\n")

    m += elems_body[i].text.replace(" ","").replace("\n","")
    t = Tokenizer()

cnt = []
token_filters = [POSKeepFilter('名詞,形容詞'), TokenCountFilter()]
a = Analyzer(token_filters=token_filters)
for k, v in a.analyze(m):
    temp = [k, v]
    cnt.append(temp)

cnt.sort(key=lambda x: x[1])
for i in cnt:
    print(i[0], ":", i[1])

"""