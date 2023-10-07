import os
import send2trash
import shutil
os.unlink('file1.txt')

# deleting a directory 
os.rmdir("python")
shutil.rmtree('python')

shutil.move("file1.txt","file2.txt")
shutil.copy()
send2trash.send2trash("python")
