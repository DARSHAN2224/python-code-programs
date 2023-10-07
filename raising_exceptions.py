# raising the exceptions
def area_rect(l,w):
    if l<=0 or w<=0:
        raise Exception("the values of l and w should be greater than 0")
    return l*w

a =int(input())
b =int(input())
try:
    area=area_rect(a,b)
except Exception as err:
    print("exception occured :",err)
else:
    print("area of rectangle :",area)