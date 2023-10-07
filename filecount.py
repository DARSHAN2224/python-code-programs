fp=open(r"A:\python lab\text.txt",'r')
con=fp.read()
d={}
for ch in con:
    d.setdefault(ch,0)
    d[ch]+=1
lst=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(len(lst)):
    print(lst[i][0],lst[i][1])
