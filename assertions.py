a,b=map(int,input().split())
try:
    assert b!=0,"divison by zero error"
    result=a/b
    print(result)
except AssertionError:
    print("assertion error")