d={"001":"hhsjh0"}
while 1:
    user_id=input("enter userid(blank to quit):")
    if user_id==" ":
        break
    elif user_id in d:
        print(f"passward of {user_id} is {d[user_id]}")
    else:
        print(f"userid is not there in the database .hence enter password of {user_id}")
        d[user_id]=input()
        