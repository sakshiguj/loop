i=int(input("enter the number"))
s=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if s==sum:
    print("it is armstrong")
else:
    print("it is not armstrong")



# i=int(input("enter the number"))
# s=i
# rev=0
# while i>0:
#     rev=rev*10+i%10
#     i=i//10
# if s==rev:
#     print("it is pallindrome")
# else:
#     print("it is not")

