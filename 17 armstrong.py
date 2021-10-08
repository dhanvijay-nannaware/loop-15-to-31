n=int(input("enter the number:"))
sum=0
var=n
while var>0:
    r=var%10
    sum=sum+r**3
    var=var//10
if sum==n:
    print("armstrong number")
else:
    print("not armstrong number")