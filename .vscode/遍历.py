'''x={'陈':1,'思':2,'未':3,'帅':4}
for i in x:
    print(x[i])'''

x=[59,70,58,60,61]
a=[]
b=[]
for i in x :
    if i>=60:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)
print(a,end='@')
print(b,end='@') 
