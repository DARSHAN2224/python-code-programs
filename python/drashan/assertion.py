# a,b=map(int,input().split())

# try:
#     assert b!=0 ,"b can not be zero"
#     c=a/b
#     print(c)
# except AssertionError as err:
#     print(err)


# num =int(input("enter a number:"))

# try :
#     assert num%2==0,"number is odd"
#     print("number is even")
# except Exception as err:
#     print(f"error is {err}")


# def area(l,b):
#     if l<=0 or b<=0:
#         raise Exception ("l and b should be +ve")
#     else:
#         return l*b

# try:
#     a=area(10,20)
#     print(a)
# except Exception as err:
#     print(err)
    
    
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(levelname)s-%(message)s")
def fact(n):
    logging.debug("start of the program")
    f=1
    for i in range(1,n+1):
        f*=i
        logging.debug(f"i is {i} fact is {f} ")
    logging.debug("factriol ended")
    return f
n= fact(5)
logging.debug(f"fact is {n}")