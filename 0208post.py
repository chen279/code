import requests
import traceback
from db import DBtool

url=input('请输入接口地址:')
d={"username":"chenchen22", "password":"a1234567", "phone":"13697934607",  "email":"11122233344@qq.com" }#也可以改成input，手动输入字典型的数据

res=requests.post(url,json=d)               #获取接口返回的一系列数据

try:
    #断言开始
    assert res.status_code==200             #用 status_code 方法返回一系列数据中的   http状态码  200   300   400   500
    assert res.json()['status']==200        #用 json 方法返回一系列数据中的字典，再用字典的 键值 提取到  开发人员设计的 工作是否成功的状态。
    #对比数据库，看数据是否修改上去了。      用到pymysql 以及封装好的  连接数据库  及  进行增删改查操作 的类
    db=DBtool(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    sql="select * from t_user where username='{}'".format(d['username'])    #sql语句
    r=db.query(sql)                         # r是运用pymysql的方法 query 查询得到的结果，这里query方法的返回值为False是，查询数据库失败。
                                            #返回值==0时，即返回了空的tuple，即没在数据库找到该名字所以len为0，如果查询结果!=0，则查询到了该用户。
    assert r!=False       # 为了判断数据库查询成功，如果不成功则数据查询失败，代码抛出异常          
    assert len(r)!=0      #判断数据库是否存在该用户，通过则表明账号已存在，不通过则报错表示不存在，表示数据添加到数据库失败。
    print('执行注册接口用例成功')
except:
    traceback.print_exc()   #返回  try   except  异常处理返回的具体报错，即会返回代码错误，也可以返回数据!=assert导致的报错 
    print('执行用例失败')