def is_ss(a):
    for i in range(2,a):
        if a%i==0:
            # print("这不是素数")
            return False
        elif i==a-1:
            # print("这是素数")
            return True