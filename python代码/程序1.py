def x_a(s):
    return s+1
def x_b(s):
    return s-1
def x_and_prnt(s,x):
    i=x(s)
    print(i)
c=int(input('c='))    
d=x_a
x_and_prnt(c,d)  
