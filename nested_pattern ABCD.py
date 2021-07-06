l=1
i=1
while i<=4:
    j=1
    while j<=4-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=l:
        print(chr(64+i),end=" ")
        k=k+1
    l=l+2
    print()
    i=i+1