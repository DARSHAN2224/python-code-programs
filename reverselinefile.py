fp=open(r'C:\c_section\counts.txt',"r")
con=fp.readlines()
fp1=open(r'C:\c_section\reverse.txt',"w")
for ch in con:
    world=ch.split()
    for i in world:
        i=i[::-1]
        fp1.write(i)
        fp1.write(' ')
    fp1.write('\n')
fp.close()
fp1.close()