import os,zipfile
# os.chdir("A:\\python class works")
zp=zipfile.ZipFile("A:\\python class works\\python.zip","r")
zp.extractall("A:\\python class works\\python")
files=zp.namelist()
print(files)
size=zp.files
zp.close()