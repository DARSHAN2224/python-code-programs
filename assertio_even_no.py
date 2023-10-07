# def is_even(n):
#     assert n%2==0,"number is not even"
#     print ("number is valid")
# num =int(input("enter a number"))
# is_even(num)



def is_even(n):
    try:
        assert n%2==0,"number is not even"
    except Exception as s:
        print(f"assertion error : {s}")
    else:
        print ("number is valid")
num =int(input("enter a number"))
is_even(num)