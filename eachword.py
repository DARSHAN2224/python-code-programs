fp=open(r"A:\python lab\text.txt",'r')
con=fp.read()
lon=''
ch=con.split()
for word in ch:
    if len(word) >len(lon):
        lon=word
# print(f"longest word is: {lon}")


# new method to find the longest worlds

words=con.split()
words.sort(key=len,reverse=True)
print(words[0])
fp.close()
