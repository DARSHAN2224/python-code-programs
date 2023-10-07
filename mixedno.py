n=int(input("enter the number"))
ev,ov=0,0
while n!=0:
    r=n%10
    if r%2==0:
        ev+=1
    else:
        ov+=1
    n=n//10
if ev==0:
    print("odd number")
elif ov == 0:
    print("even number")
else:
    print("mixed number")