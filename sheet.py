alpha = 'abcdefghijklmnopqrstuvwxyz'
new = ''
current_shift = 12
current_char = 0
d = ''
for i in range(0,len(alpha)):
	print(alpha[i] + " --> " + alpha[current_shift + i])
	new+=(alpha[current_shift + i])
	if i % 3 == 0 or i % 3 == 1:
		current_shift -=10
	else:
		current_shift+=16


a = ""
k = 'mrkcdpmsuimzstqrlg'
for c in range(0, len(k)):
	i = new.find(k[c])
	a += alpha[i]
print(k + "-->" + a)