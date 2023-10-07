age=int(input("enter the age of the person"))
aa=input("enter the 12  digits aadhar number")
if aa.isnumeric() and len(aa)==12:
    if(age>=18):
        print("can vote")
    else:
        print("not eligible t vote")
else:
    print("invalid aadhar number")