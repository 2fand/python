ok=True
x=[]
for ib in range(10):
    x.append(str(ib))
i=input('请输入一个值：')
a=len(i)
if a==0:
    print('此值不是一个正整数')
else:
    for ia in i:
        if ia not in x:
            ok=False
    if not ok:
        print('此值不是一个正整数')
    else:
        if a==1:
           print('此值是一个正整数')
        else:
            if i[0]=='0':
                print('此值不是一个正整数')
            else:
                print('此值是一个正整数')