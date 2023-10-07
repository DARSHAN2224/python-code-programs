fp=open(r'C:\c_section\counts.txt',"r")
con=fp.read()
print(con)
fp1=open(r'C:\c_section\reverse.txt',"w")
world=con.split()
for i in world:
    i=i[::-1]
    fp1.write(i)
    fp1.write(' ')
print(world)
fp.close()
fp1.close()