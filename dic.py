# write a python progarm to store birthdays of employees 
# if the name of the employee searched by the user is not present in the dictanory .
# ask to user to update the birth day  by taking the input from the user
d={"cs12":"16.7.2004"}
while 1:
    name=input("enter name(blank to quit):")
    if name==" ":
        break
    elif name in d:
        print(f"birthday of {name} is {d[name]}")
    else:
        print(f"name is not there in the database .hence enter birthday of {name}")
        d[name]=input()
        
        