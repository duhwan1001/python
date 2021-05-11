import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='java',
                       db='python', charset='utf8')
 
tuts = (
        ('1', '1', '1'),
        ('2', '2', '2'),
        ('3', '3', '3')
        )

curs = conn.cursor()

sql = "INSERT INTO hello (col01,col02,col03) VALUES (%s,%s,%s)"  # insert
cnt = curs.executemany(sql, tuts)  # insert value # 다중행 반영할때는 executemany

print(str(cnt) + "개의 행이 반영되었습니다")
conn.commit()
rows = curs.fetchall()


conn.close()
