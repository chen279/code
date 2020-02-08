import traceback
from db import DBtool
import requests  # get方法，导入requests，自动化进行接口测试以及去数据库验证
                 # requests  包用于http请求的第三方包



url=input('请输入接口地址:')             #'http://192.144.148.91:2333/showversion'，查看版本号接口。
res=requests.get(url)
                                        #print(res.text)    将返回的乱码内容，用text储存为一个文件。
assert res.status_code==200             # 将接收的数据中的  http状态码  提取出来   判断http请求是否正常
                                        #  200表示正常  300多表示重定向  400多表示  请求端错误   500多表示  服务器端错误
r=res.json()                            #将返回内容中的  字典提取出来
assert r.get('status')==200             #判断接口返回的值是否等同于开发给的接口文档的值
print('测试通过')

                                        #assert表示断言，即if判断语句，断言内容成立，不返回值，程序继续向下运行
                                        #                             断言内容不成立，则报错，程序不向下运行

                                        #规避异常用  try:  缩进  except:  
                                        # http状态码决定能不能工作
                                        #接口返回的同接口文档规定的值做的对比  决定工作是否做成功