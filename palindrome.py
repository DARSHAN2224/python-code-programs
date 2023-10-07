n=int(input("enter the number"))
s,t=0,n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if t==s:
    print("palindrome")
else:
    print("not palindrome")