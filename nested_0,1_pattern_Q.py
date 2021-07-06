# l=1
# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     k=1
#     while k<=i:
#         print(1,end=" ") 
#         k=k+1
#     l=i   
#     while l>0:
#         print(0,end=" ") 
#         l=l-1     
#     print() 
#     i=i+1 



n=1
i=1
while i<=5:
    k=1
    while k<=5-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print("1",end=" ")
        print("0 1",end=" ")
        j=j+1
    n=n+2
    print()
    i=i+2

# l=1
# i=5
# while i<=7:
#     j=1
#     while j<=i:
#         print(" ",end=" ")
#         j=j+1
#     k=i
#     while k<=i:
#         if k%2==0:
#             print("0",end="") 
#         else:
#             print("1",end="") 
#     l=l+2
#     print()  
#     i=i-1 