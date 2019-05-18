def ishw(a):
    b=str(a)
    for i in range(1,int(len(b)/2)+2):
        if b[i-1]!=b[-i]:
            print("这不是回文数")
            break
        elif i==int(len(b)/2)+1:
            print("这是个回文数")
ishw(123421)