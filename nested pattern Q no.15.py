# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<=i:
#         print("*",end=" ") 
#         k=k+1   
#     print()
#     i=i+1 

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=5-i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1

#     i+=1
n=int(input("enter the number"))
i=1
j=1
while i<=6:
    while i<=n:
        print(" "*(n-j),"*"*i)
        j=j+1
        i=i+2


