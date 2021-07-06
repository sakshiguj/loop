num=int(input("enter the number"))
i=1
while i<=1:
    if num%2!=0:
        print("weird")
    elif num%2==0 and num>2 and num<5:
        print("not weird") 
    elif num%2==0 and num>6 and num<20:
        print("weird")
    elif num%2==0 and num>20:
        print("not weird")    
    else:
        print(i) 
    i=i+1 