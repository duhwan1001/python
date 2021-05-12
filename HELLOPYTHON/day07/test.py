import numpy as np
import matplotlib.pyplot as plt
import pymysql
    
conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
 
curs = conn.cursor()
sql = """
    SELECT s_name 
    FROM stock
    """

curs.execute(sql)

ret = []
rows = curs.fetchall()
for row in rows:
    ret.append(row[0])
print(ret)
conn.close()
