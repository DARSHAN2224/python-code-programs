n=int(input("enter a number:"))
ec,oc=0,0
while n!=0:
    r=n%10
    if r%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10

if ec==0:
    print("strictly odd")
elif oc==0:
    print("strictly even")
else:
    print("mixed number")