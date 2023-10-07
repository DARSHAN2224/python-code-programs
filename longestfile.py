fp=open(r'C:\c_section\counts.txt',"r")
con=fp.read()
# print(con)
world =con.split()
max=""
# d={}
for ch in world:
    if len(ch)>len(max):
        max=ch
print(max)
# for ch in world:
#     d[ch]=len(ch)
# n=list(d.keys())
# m=list(d.values())
# pos=m.index(max(m))
# print(n[pos])
fp.close()