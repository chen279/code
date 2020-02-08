import pymysql
class DBtool():
    def __init__(self,host='192.168.242.129',user='root',password='123456',db='test'):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
      
    def query(self,sql):
        try:
            db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
            cursor = db.cursor()    #获得 游标
            cursor.execute(sql)     #执行查询语句
            res = cursor.fetchall() #获取查询结果  返回的是元组   查询成功返回元组，查询失败返回False
            db.close()              #关闭连接
            return res
        except:
            return False

    def commit(self,sql):
        try:
            db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
            cursor = db.cursor()    #获得游标
            cursor.execute(sql)     #执行  增 删 改  语句
            db.commit()             #提交修改
            db.close()              #关闭连接
            return True
        except:
            return False