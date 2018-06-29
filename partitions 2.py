from math import ceil

def p(n, k, l, s):
	print(n,k,l,s)
	if n < 0 or  k < 0  or  l < 0  or s < 0:
		return 0
	if n == 0:
		return 1
	if k == 0 or l == 0:
		return 0
	if k > n:
		return p(n, n, l, s)
	if l > n:
		return p(n, k, n, s)
	if s > n:
		return p(n, k, l, n)
	return  p(n, k - 1, l, s) + p(n, k, l - 1, s) - p(n, k - 1, l - 1, s)+ p(n - k - l + 1, k - 1, l - 1, s + l - k - 1)

#P(n - k - l + 1, k - 1, l - 1, s + l - k - 1)
n = 920
k = 436
l = 3
s = l-1
print(p(n - k - l + 1, k - 1, l - 1, l-1))