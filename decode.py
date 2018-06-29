string = ""
file = open("plain.txt", "r")
lines = file.read().splitlines()
for line in lines:
	string+=chr(int(line))
print(string)