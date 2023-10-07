import os,zipfile
zp=zipfile.ZipFile("python.zip")
name=zp.namelist()
print(name)
file1=zp.getinfo("file3.txt")
size=file1.file_size

print(size)
zp.close()

#creating a zip file
newzip=zipfile.ZipFile("phy.zip",'w')
newzip.write("C:\\c_section\\counts.txt",compress_type=zipfile.ZIP_DEFLATED)

#extracting a zipfile 
zp=zipfile.ZipFile("python.zip","r")
zp.extract("file1.txt")



zp=zipfile.ZipFile("phy.zip","r")
zp.extractall()
zp.close()
# newzip.close()
