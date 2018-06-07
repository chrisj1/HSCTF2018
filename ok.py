num = 0
for i in range(0, 999):
	if i % 2 == 0:
		num = num * 2 + 1
	else:
		num = num * 2 - 1
print(num%(10**9 + 7))