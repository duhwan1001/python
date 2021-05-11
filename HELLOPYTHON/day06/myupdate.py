import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
curs = conn.cursor()
 
sql = """UPDATE hello SET col02 = '5', col03 = '5' WHERE col01 = 2"""  # update # " 3개 사용시 줄바꿈 안해도 됨
cnt = curs.execute(sql)  # insert value

conn.commit()
rows = curs.fetchall()

print(str(cnt) + "개의 행이 반영되었습니다")

conn.close()
