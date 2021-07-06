n=int(input("enter the number"))
i=1
j=1
while i<=6:
    while i<=n:
        print(" "*(n-j),"*"*i)
        j=j+1
        i=i+2