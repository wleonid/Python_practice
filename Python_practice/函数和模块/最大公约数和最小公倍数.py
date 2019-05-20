def gys(a,b):
    if a>b:
        c=a
        b=c
        a=b
    for i in range(b,0,-1):
        if a%i==0 and b%i==0:
            return i

def gbs(a,b):
    c=gys(a,b)
    return a*b/c

print(gys(14,21),gbs(14,21))