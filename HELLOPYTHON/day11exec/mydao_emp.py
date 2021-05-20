import pymysql

class DaoEmp :
    
    def __init__(self):
        self.conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
        )
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor() 

        sql = "SELECT e_id, kor, eng, math FROM exam;"
        curs.execute(sql)

        result = curs.fetchall()

        for row in result:
            ret.append({"e_id":row[0],"kor":row[1],"eng":row[2], "math":row[3]})
            
        return ret
            
    def myinsert(self, e_id, kor, eng, math):
        curs = self.conn.cursor() 

        sql = "INSERT INTO EMP(e_id, kor, eng, math) VALUES({},{},{},{});".format(e_id, kor, eng, math)
        cnt = curs.execute(sql)

        self.conn.commit()
        
        return cnt
    
    def myupdate(self, e_id, kor, eng, math):
        
        curs = self.conn.cursor() 

        sql = f"""
                UPDATE exam
                SET 
                kor='{kor}', 
                eng='{eng}',
                math='{math}'
                WHERE
                e_id='{e_id}'
            """
        
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def mydelete(self, e_id):
        curs = self.conn.cursor() 

        sql = f"DELETE FROM exam WHERE e_id = '{e_id}'"
        
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.conn.close()
        
if __name__== '__main__':
    de = DaoEmp()
    
    list = de.myselect()
    # cnt = de.myinsert('4','3','3')
    # cnt = de.myupdate('4','6','6')
    cnt = de.mydelete('4')
    
    print(list)
    print(cnt)
    