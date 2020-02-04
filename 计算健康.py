
A=(input('请输入身高：'))
a=float(A)
B=(input('请输入体重：'))
b=float(B)
if 0<b/a**2 < 18.5 :
    print('过轻')
elif b/a**2 <=25:
    print('正常')
elif b/a**2 <=28:
    print('过重')
elif b/a**2 <=32:
    print('肥胖')
else :
    print('严重肥胖')


