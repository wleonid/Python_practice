for i in range(1,10000):
    sy=[]
    s=0
    for j in range(1,i):
        if i%j == 0:
            sy.append(j)
    for k in sy:
        s=s+k
    if i==s:
        print(s)
    s=0
    sy=[]