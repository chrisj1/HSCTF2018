s = "mrkcdpmsuimzstqrlg"
r = ""
for i in range(0, len(s)):
	ch = s[i]
	num = ord(ch)
	if i % 3 == 0:
		num -= 10
	else:
		num += 16
	r += chr(num)
print(r)