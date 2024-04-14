import random
import time
'''
x1=random.randint(1,10000)
x2=[]
print(x1)
for i in range(1,x1):
    if x1%i==0:
        x2.append(i)
x2.append(x1)
print(x2)
'''
#能输出一个数和这个数的因数的程序（列表）^
'''
i=random.randint(1,10000)
if i%2==0:
    print(f'{i}是偶数')
else:
    print(f'{i}是奇数')    
'''
#能判断一个数是奇数还是偶数的程序^ 
'''
i=1
x=random.randint(1,300)
for ia in range(1,x+1):
    i*=ia
print(f'{x}!={i}') 
'''
#能输出一个数的阶乘的程序^
'''
x=8
y=10
z=3
i=[0]*x   
for ia in range(x):
    i[ia]=[0]*y
for a in range(x):
    for b in range(y):
        i[a][b]=[None]*z
for g in i:
    print(g) 
'''
#三维列表^
'''
data='OX'
for ia in range(9):
    i=[]
    for ib in range(9):
        i.append(random.choice(data))
    print(i)
'''
#输出一个只带有“X”和“O”的随机二维列表^
'''
a=1
b=1232542452367
print(f'a={a},b={b}')#<--------------------------!!!
b+=a
a=b-a
b-=a
print(f'a={a},b={b}')#<--------------------------!!!
'''
#能将两个变量里的数字交换一下的程序^
'''
with open('Desktop\\(请改一下名字).py','w',encoding='utf-8'):
    a=0#<----------------------------无用代码
'''
#能创建一个py文件的程序^
'''
x=[]
for ia in range(10000):
    x1=ia+1
    x2=[]
    for i in range(1,x1):
        if x1%i==0:
            x2.append(i)
    x2.append(x1)
    if len(x2)==2:
        x.append(x1)
print(f'10000以内的质数:{x}')        
'''
#打印10000以内的质数^
'''
print('加载中...')
ex=x=[]
for ia in range(10000):
    x1=ia+1    
    time.sleep(0.005)
    x2=[]
    for i in range(1,x1):
        if x1%i==0:
            x2.append(i)
    x2.append(x1)
    x.append(len(x2))
    x2=[]    
for ib in range(10000):
    ex.append(str(ib+1))
print('已加载完成！')
time.sleep(1.02)
i=input('你要查询哪个数的因数的数量?(只能输入1~10000之中的其中的一个数字)  ')
if i in ex:
    i=int(i)
    print(f'你所查询的“{i}”有{x[i-1]}个因数')
else:
    print('抱歉，我无法回答你回答的东西的因数的数量')
'''
#能查询哪个数的因数的数量的程序（有关于加载的基础程序）^
'''
with open('Desktop\\斐波那契数列.txt','w',encoding='utf-8') as f:    
    x=[]
    for i in range(2):
        x.append(i)
    for ia in range(9998):
        x.append(x[(len(x)-1)]+x[(len(x)-2)])
    for ib in x:
        f.write(f'{ib}\n')
    print('OK!')            
'''
#创建一个只有10000个数的名叫“斐波那契数列.txt”的文件（里面的数字是斐波那契数列里的数字）^   
'''
a=3.1232
print("\'\"\'")
print(f'{a:.3}')
print('{0:.2}'.format(a))
print('{b:.0f}'.format(b=a))
print("\'\"\'")
'''
#奇妙的打字^    