import pyperclip
txt=pyperclip.paste()
txt1=""
lines=txt.split('\n')
for line in lines:
    line="* " + line
    txt1+=line+'\n'
pyperclip.copy(txt1)
print(txt1)