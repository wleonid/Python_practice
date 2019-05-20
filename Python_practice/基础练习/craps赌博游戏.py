import random

#随机出点数
i1= random.randint(1,6)
i2= random.randint(1,6)
#对点数进行判断，如果点数和为2、3或12，则玩家输，如果和为其它点数，则记录第一次的点数和，然后继续掷骰，直至点数和等于第一次掷出的点数和，则玩家胜，如果在这之前掷出了点数和为7，则玩家输。
i3=i1+i2
print(i1,i2)
if i3==7 or i3==11:
    print(i1,i2,"Win")
elif i3==2 or i3==3 or i3==12:
    print(i1,i2,"Lose")
else:
    i1= random.randint(1,6)
    i2= random.randint(1,6)
    print(i1,i2)
    while True:
        if i1+i2==i3 :
            print(i1,i2,"Win",11)
            break
        elif i1+i2==7:
            print(i1,i2,"Lose")
            break
        i1= random.randint(1,6)
        i2= random.randint(1,6)
        print(i1,i2)