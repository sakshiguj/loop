i=int(input("enter the number"))
s=i
rev=0
while i>0:
    rev=rev*10+i%10
    i=i//10
if s==rev:
    print("it is pallindrome")
else:
    print("it is not")

