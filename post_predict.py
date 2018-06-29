f = open('predicted.txt', 'r').read().splitlines()

for i in range(1,33):
	if int(f[i]) % 2 == 0:
		print('L')
	else:
		print('Y')