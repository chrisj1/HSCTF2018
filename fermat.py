

for a in range(1, 500):
	print(a)
	for b in range(1, 500):
		for c in range(1, 500):
			if (a*a*a + b*b*c == c*c*c):
				print(a,b,c)
