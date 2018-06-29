#construct the integer
nums = []
strings = []
f = open("l.txt", "r").read().splitlines()
for i in range(0, len(f), 32):
	s = f[i:i+32]
	s.reverse()
	st = ""
	for elem in s:
		if elem is 'Y':
			st += "1"
		else:
			st += "0"
	strings.append(st)
for i in range(0, 625):
	num = int(strings[i],2)
	nums.append(num)
	print(num)