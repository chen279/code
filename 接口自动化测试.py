
#用requests就是用来自动上传数据，     然后用pymysql连接数据以查询对比数据，看测试是否成功


import requests
from db import DBtool
import traceback

'''url=input('请输入接口地址')
a=input('请输入注册账号:')
b=input('请输入注册密码:')
c=input('请输入注册手机号:')
d=input('请输入注册邮箱:')
d={'username':a,'password':b,'phone':c,'email':d}#该数据根据测试文档及用例来'''

url='http://192.144.148.91:2333/regist'   #注册接口地址url
d={"username":"chenchen31", "password":"a1234567", "phone":"13697934607",  "email":"11122233344@qq.com" }#也可以改成input，手动输入字典型的数据

res=requests.post(url,json=d)                    #res  是用requests请求回来的数据   json=d表示post上传的  字典型数据
                                                 #在上传数据


# assert断言操作，相当于if，如果不成立则报错，然后不向下运行。
try:
    assert res.status_code==200                  #用status_code方法返回一系列数据中的http状态码 正常200  重定向300  请求端错误400  服务器端错误500
    assert res.json()['status']==200             #json  方法返回的是所有数据中的 字典数据  ，再用键值法取出来  开发设计的‘status’码，然后与设计的数字对比

    db=DBtool(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")   #用已经封装好的方法连接数据库
    sql="select * from t_user where username='{}'".format(d['username'])   

    r=db.query(sql)                     #通过封装的类引用的 pymysql 查询数据库中是否有和我们注册输入一样的数据。
                                        #返回的值均在  DBtool中得到定义
                                        #查询语句有问题则返回False,!=False则是查询数据成功，然后len(r)==0，则没查询到，len(r)!=0，则表明查询到相同的数据
    assert r !=False    #判断是否查询这件事是否失败，失败了则不向下运行并且报错，不报错则说明查询这件事没问题，然后继续向下运行。
    assert len(r) !=0        #判断是否为0，assert通过说明不为零，即上传数据成功了，测试成功。如果不通过说明为零，说明测试失败了，数据没进数据库。
    print('执行用例成功')   #所有assert断言通过了，执行到最下面，说明，查询到数据库有我们添加的数据了，说明测试成功

except:
    traceback.print_exc()   #返回  try   except  异常处理返回的所有报错，包括代码问标以及数据导致的assert的断言问题
    print('执行用例失败')   