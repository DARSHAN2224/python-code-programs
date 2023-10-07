import shelve
fp=shelve.open("data")
lst=[1,2,3,4,5,6,7]
# fp["lst"]=lst
mv=10
# fp["mv"]=mv
# fp["interest"]=4.5
print(fp['mv'])
print(fp['lst'])
fp.close()

