def printboard(d):
    print(d["tl"]+"|"+d["tm"]+"|"+d["tr"])
    print('-+-+-')
    print(d["ml"]+"|"+d["mm"]+"|"+d["mr"])
    print('-+-+-')
    print(d["bl"]+"|"+d["bm"]+"|"+d["br"])
board={"tl":" ","tm":" ","tr":" ",
       "ml":" ","mm":" ","mr":" ",
       "bl":" ","bm":" ","br":" "}



board["tl"]="o"
board["tr"]="x"
board["m1"]="x"
board["mm"]="o"
board["br"]="o"

printboard(board)