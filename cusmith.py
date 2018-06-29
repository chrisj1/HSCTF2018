from math import gcd
import gmpy
file = open("nums.txt", "r")

lines = file.read().splitlines()

ns = []
cs = []
es = []

for line in lines:
	if line[:1] == "n":
		n = int(line[4:])
		ns.append(n)
	if line[:1] == "c":
		c = int(line[4:])
		cs.append(c)
	if line[:1] == "e":
		e = int(line[4:])
		es.append(e)

for i in range(0, len(ns)):
	for j in range(i, len(ns)):
		g = gcd(ns[i], ns[j])
		if g != ns[i] and g !=  ns[j]:
			n1 = ns[i]
			n2 = ns[j]
			p = gcd(ns[i], ns[j])
			q1 = gmpy.divexact(n1,p)
			q2 = gmpy.divexact(n2,p)
			c1  = cs[i]
			c2 = cs[j]
			e1 = es[i]
			e2 = es[j]
			if p == 1: continue
			print("p = {} \n q1 = {}  \n q2 = {} \n n1 = {} \n n2 = {} \n c1 = {} \n c2 = {}, e1 = {}, e2 = {}".format(p, q1, q2, n1, n2,c1, c2, e1, e2))
			q = q1
			e =e1
			phin = (p-1) * (q-1)
			d = gmpy.invert(e,phin)
			print(d)
			c = c1
			y = pow(c,d,n1)
			print()
			print()
			print(y)
			print()