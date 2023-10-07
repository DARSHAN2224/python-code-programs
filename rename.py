import os 
path1=input("enter the path:")
lst=os.listdir(path1)
os.chdir(path1)
for file in lst:
    if file.endswith(".txt"):
        newname=file.split('.')[0]+".csv"
        os.rename(file,newname)
        print(f"renamed file {file} to {newname  }")


# import os 
# def change(path):
#     for root,dirs,files in os.walk(path):
#         for file in files:
#             if file.endswith(".txt"):
#                 file_path=os.path.join(root,file)
#                 new_file_path=os.path.splitext(file_path)[0]+'.csv'
#                 os.rename(file_path,new_file_path)
#                 print(f"renamed file {file_path} to {new_file_path}")
# lst=os.listdir("python")
# change("python")
                
            
# import os 
# def change(path):
#     # for root,dirs,files in os.walk(path):
#     # for file in files:
#     print(path)
#     if path.endswith(".txt"):
#         # file_path=os.path.join(root,file)
        
#         new_file_path=os.path.splitext(path)[0]+'.csv'
#         os.rename(path,new_file_path)
#         print(f"renamed file {path} to {new_file_path}")
# lst=os.listdir("python")
# change("python\\file1.txt")
                