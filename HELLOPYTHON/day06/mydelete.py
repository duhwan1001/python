import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """DELETE FROM hello WHERE col01 = 1"""
cnt = curs.execute(sql)

conn.commit()
rows = curs.fetchall()

print(str(cnt) + "개의 행이 반영되었습니다")

conn.close()
