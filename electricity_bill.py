units=int(input("enter the units consumed"))
if units<=199:
    bill=units*1.20
elif units<400:
    bill=units*1.50
elif units<600:
    bill=units*1.80
else:
    bill=units*2.00

if bill>400:
    surchar=bill*0.15
else:
    surchar=100
total_bill=bill+surchar
print("The amount to be paid",total_bill)