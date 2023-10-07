import os
import sys 
os.makedirs('python')
if os.path.isdir('python'):
    print("directory created")
else:
    print("directory creation failed")
    sys.exit(0)
os.chdir("python")
fp1=open("file1.txt",'w')
fp2=open("file2.txt",'w')
fp3=open("file3.txt",'w')

fp1.write("harsh is a good boy")
fp2.write("harsh is a bad boy")

fp1=open("file1.txt",'r')
con1=fp1.read()
fp2=open("file2.txt",'r')
con2=fp2.read()
fp3.write(con1+"\n"+con2)
fp1.close()
fp2.close()
fp3.close()