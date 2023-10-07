import zipfile,os
folder =input("enter the name of folder")
os.chdir("A:\\python class works\\python\\new folder")
folder=os.path.abspath(folder)
base_name=os.path.basename(folder)
zip_file=base_name+".zip"
zp=zipfile.ZipFile(zip_file,"w")
for fln,sf,fn in os.walk(folder):
    for fns in fn:
        file_path=os.path.join(fln,fns)
        zp.write(file_path,os.path.relpath(file_path,folder))
zp.close()