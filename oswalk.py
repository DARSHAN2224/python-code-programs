import os
for foldername,subfolders,filesnames in os.walk("A:\\python class works\\python"):
    print("the root folder is ",foldername)
    # print("the subfolder is",subfolders)
    # print("the filename is",filesnames)
    for subfolder in subfolders:
        print('subfolder of'+foldername+':'+subfolder)
    for filename in filesnames:
        print("file inside "+foldername+":"+filename)
    print() 