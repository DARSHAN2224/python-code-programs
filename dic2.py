# write a python progarm to store country name and captial for minimum  5 countries and 
# display the name of countires and their captial in sotred order 

d={}
print("enter five counties and captial")
for i in range(5):
    country ,captial=map(str,input().split())
    d[country]=captial
    
sd=sorted(d)
print("="*40)
print(f'{"country":15s}{"captial":15s}')
print("="*30)
for i in sd:
    print(f"{i:15s}{d[i]:15s}")