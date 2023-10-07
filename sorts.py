lst1=['b','r','g','a','k','m','as']
lst2=[10,3,4,6,8,2,1]
d={}
for i in range(len(lst1)):
    d[lst2[i]]=lst1[i]
d=sorted(d.items())

for i in d:
    print(i[0],i[1])
