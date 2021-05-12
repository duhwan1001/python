import numpy as np
import matplotlib.pyplot as plt
import pymysql


def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
     
    curs = conn.cursor()
    sql = """
        SELECT s_price 
        FROM stock 
        WHERE s_name = '{}'
        """.format(s_name)
    
    curs.execute(sql)
    
    rows = curs.fetchall()
    for row in rows:
        ret.append(row[0])
    
    conn.close()
    return ret
    

fig = plt.figure()
ax = plt.axes(projection='3d')

z_sam = np.array(getPrices("삼성전자"))
z_samr = np.array(getPrices("동아에스티"))
z_kia = np.array(getPrices("기아"))
x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  # 12개

ax.set_title('chart test')
ax.plot3D(x, y, z_sam, 'maroon')  # x , y , color
ax.plot3D(x + 1, y, z_samr, 'blue') 
ax.plot3D(x + 2, y, z_kia, 'orange') 
plt.show()
