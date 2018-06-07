D = {}
def P(n,s,x):
  if n > s*x or x <= 0: return 0
  if n == s*x: return 1
  if (n,s,x) not in D:
    D[(n,s,x)] = sum(P(n-i*x, s-i, x-1) for i in xrange(s))
  return D[(n,s,x)]


#parse file
key = []
f = open('partition.txt', 'r').read().splitlines()
for line in f:
	l = line.split(" ")
	n = l[0]
	k = l[1]
	nk = [n,k]
	key.append(nk)

total = 0
print('calculate')
for elem in key:
	n = int(elem[0])
	k = int(elem[1])
	for i in range(3, n-k, 2):
		total += P(n, i, k)
		print(total)