from bs4 import BeautifulSoup
import requests
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
import re
import time
"""
コードの大まかな流れ

1.HTMLのソースを取得
↓
2.HTMLの[st-pg_contents]クラスから最終ページを取得
↓
3.ページを最終ページまで更新しながら解析用stringの変数へ追加していく
↓
4.string変数を解析して含まれている単語を分析
"""

get_url_info = requests.post('https://dic.nicovideo.jp/b/a/%E5%8D%AF%E6%9C%88%E3%82%B3%E3%82%A6/1-')#対象ページへリクエストを送信
soup = BeautifulSoup(get_url_info.text, 'html.parser')#THMLソースを形態素解析できる形に変換

elems_page = soup.select('.st-pg_contents')#HTMLソースのうち[st-pg_contens]のクラスに属する要素のみを取得
page_no = re.findall('[0-9]+', elems_page[0].text)
#[elmes_page[0].text]:elems_pageはHTMLソースにある[st-pg_contents]の個数分の要素を持つ配列
#[st-pg_contents]クラスはヘッダーとフッターにある同じものなので今回はヘッダーだけ取っておけばいい
#ヘッダーは一個目の要素に含まれていてフッターは二個目の要素に含まれている
#ヘッダとフッタは同じなので今回はヘッダだけ使う
#re.findallは[elems_page[0].text]から指定の文字列を抜き出す関数。今回は正規表現で[0-9]+とすることで数字列を取得している
#page_noは配列になっていてそれぞれの要素には各ページの先頭掲示板番号が代入されている
last = int(page_no[len(page_no) - 1])#最終ページの先頭掲示板番号はpage_noの最後の要素に入っているのでそれをlast変数に格納。intに型変換

page_title = 'https://dic.nicovideo.jp/b/a/%E5%8D%AF%E6%9C%88%E3%82%B3%E3%82%A6/'
all_text = ''

for page in range(0, last, 30):
    print(page + 1)
    get_url_info = requests.post(page_title + (str)(page + 1))#
    soup = BeautifulSoup(get_url_info.text, 'html.parser')#

    elems_no = soup.select('.st-bbs_resNo')#
    elems_info = soup.select('.st-bbs_resInfo')#
    elems_body = soup.select('.st-bbs_resbody')#
    
    """
    with open('test.txt', 'w'):#
        pass#

    for i in range(len(elems_no)):#
        with open('test.txt', mode='a',encoding='utf_8') as f:#
            f.write(elems_no[i].text.replace(" ","").replace("\n",""))#
            f.write("\n")#
            f.write(elems_info[i].text.replace(" ","").replace("\n",""))#
            f.write("\n")#
            f.write(elems_body[i].text.replace(" ","").replace("\n",""))#
            f.write("\n")#
    """
    for i in range(len(elems_no)):
        all_text += elems_body[i].text.replace(" ","").replace("\n","")#
        t = Tokenizer()#
    
    time.sleep(5)

cnt = []#
token_filters = [POSKeepFilter('名詞'), TokenCountFilter()]#
a = Analyzer(token_filters=token_filters)#
for k, v in a.analyze(all_text):#
    temp = [k, v]#
    cnt.append(temp)#

cnt.sort(key=lambda x: x[1])#
for i in cnt:#
    print(i[0], ":", i[1])#

