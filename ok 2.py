def countO(string):
	run = False
	last = 'k'
	count = 0
	for c in string:
		if c is 'o':
			if last is 'o':
				if not run:
					count += 1
					run = True
		else:
			run = False
		last = c
	return count


num = 0
count = 0
while count < 999:
	new = num * 2
	if count % 2 == 0:
		new +=1
	else:
		new -= 1
	#print(new)
	num = new
	count +=1

print(num % ((pow(10,9))+7))
##message = 'k'
##num = 0
##while num < 100:
##	new = ""
##	for c in message:
##		if c is 'k':
##			new += 'ok'
##		else:
##			new += 'ko'
##	print(countO(new))
##	message = new
##	num+=1
##