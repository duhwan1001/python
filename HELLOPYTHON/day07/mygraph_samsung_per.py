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
    return np.array(ret)

def getNames():
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
     
    curs = conn.cursor()
    sql = """
            SELECT s_name 
            FROM stock
            GROUP BY s_name
            LIMIT 10
        """
    
    curs.execute(sql)
    
    names = []
    rows = curs.fetchall()
    for row in rows:
        names.append(row[0])
    conn.close()
    return names

arr_name = getNames()
print(arr_name)

arrz = []
arr_per_z = []
for i in range(len(arr_name)):
    print(i)
    arrz.append(getPrices(arr_name[i]))
    
    arr_per_z.append(arrz[i]/arrz[i][0])

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  # 12개

for i in range(len(arr_name)):
    ax.plot3D(x+i, y, arr_per_z[i])  # x , y , color
    
ax.set_title('chart test')
plt.show()
