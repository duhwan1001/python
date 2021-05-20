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

        sql = "SELECT e_id, e_name, birth FROM emp;"
        curs.execute(sql)

        result = curs.fetchall()

        for row in result:
            ret.append({"e_id":row[0],"e_name":row[1],"birth":row[2]})
            
        return ret
            
    def myinsert(self, e_id, e_name, birth):
        curs = self.conn.cursor() 

        sql = "INSERT INTO EMP(e_id, e_name, birth) VALUES({},{},{});".format(e_id, e_name, birth)
        cnt = curs.execute(sql)

        self.conn.commit()
        
        return cnt
    
    def myupdate(self, e_id, e_name, birth):
        json = {
                'e_name' : '2',
                'e_id' : '7',
                'birth' : '7'
            }
        
        curs = self.conn.cursor() 

        sql = f"""
                UPDATE EMP
                SET 
                e_name='{e_name}', 
                birth='{birth}'
                WHERE
                e_id='{e_id}'
            """.format(e_name, birth, e_id)
        
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def mydelete(self, e_id):
        curs = self.conn.cursor() 

        sql = f"DELETE FROM EMP WHERE e_id = '{e_id}'"
        
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
    