fp=open(r'C:\c_section\counts.txt',"r")
con=fp.read()
print(con)
vc=cc=lc=wc=scc=nc=0
wc=len(con.split())
lc=len(con.split("\n"))
for s in con:
    if s.isalpha():
        if s in 'aeiouAEIOU':
            vc+=1
        else:
            cc+=1
            
    elif s.isdigit():
        nc+=1
            
    else:
        scc+=1

print(f'vowel count is {vc}')
print(f'consonant count is {cc}')
print(f'line count is {lc}')
print(f'words count is {wc}')
print(f'number count is {nc}')
print(f'special charcter count is {scc}')
fp.close()