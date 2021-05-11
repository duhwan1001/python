# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request

from bs4 import BeautifulSoup
import pymysql


def insertChicken(tuts):
     
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
     
    curs = conn.cursor()
    sql = "INSERT INTO chicken (title, link, description, bloggerName, bloggerLink, postdate) VALUES (%s,%s,%s,%s,%s,%s)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

client_id = "WeFwAwyXZHRxG2Cu8wJU"
client_secret = "pRcAnKAfBf"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'xml')
    
    items = soup.select("item")
    
    tuts = []
    for i, item in enumerate(items):
        title       = item.title.text
        link        = item.link.text
        description = item.description.text
        bloggerName = item.bloggername.text
        bloggerLink = item.bloggerlink.text
        postdate    = item.postdate.text
        
        tuts.append((title, link, description, bloggerName, bloggerLink, postdate))
        
    cnt = insertChicken(tuts)
    print("cnt", cnt)
else:
    print("Error Code:" + rescode)
    