# n=int(input("enter the number"))
# s,t=0,n
# while n!=0:
#     r=n%10
#     s+=r**3
#     n=n//10
# if t==s:
#     print("armstrong ")
# else:
#     print("not armstrong ")


n=int(input("enter the n value"))
s,t=0,n
while n!=0:
    r=n%10
    s+=r**3
    n=n//10
if t==s:
    print("armstrong number")
else:
    print("not armstrong number")