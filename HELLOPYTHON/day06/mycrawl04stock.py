from datetime import datetime
from urllib.request import urlopen

from bs4 import BeautifulSoup   
import pymysql

import time


def insertCrawl(tuts):
     
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
     
    curs = conn.cursor()
    sql = "INSERT INTO stock (s_name, s_price, s_code, crawl_date) VALUES (%s,%s,%s,%s)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

for i in range(10):
    html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
    bsObject = BeautifulSoup(html, "html.parser")
    name = bsObject.select("td.st2 > a")
    price = bsObject.select("td.st2 + td")
    code = bsObject.select("td > span")
    nametut = []
    pricetut = []
    codetut = []
    for s_name in name:
        nametut.append(s_name.get_text()) 
    for s_price in price:
        pricetut.append(s_price.get_text().replace(",", "")) 
    for s_code in code:
        codetut.append(s_code.get_text()) 
    crawlDate = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    tuts = []
    for i in range(1, len(nametut)):
        tuts.append((nametut[i], pricetut[i], codetut[i], crawlDate))
    cnt = insertCrawl(tuts)
    print("cnt", cnt)   
    
    time.sleep(60) # 자바와 다르게 default가 초 단위임
