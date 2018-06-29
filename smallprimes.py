from math import gcd
import random
import gmpy

num = 0x74bf4fc2d66d08c0ac7d66d90e21b16b4c0d01b1e04c40fcc2ee8ee622dff02a03f9ac98027bfff7c119894e581af56ff997e4ee2123e8137e5b7771d02f208f0f47165c76150308fd7a1d47bb91e67a608a56b12f786d04cb59a15515af5d414f809c4f3564f35ed6b28e35aaf9dc3d88dda2609ece39edfc9d081e816a7c86173b26dfe4f48835c69a55a8c5a6f851fc617eee2c3b1f81bf7c0fed7c24adb345d2cfe8fa6e00b7f0cdbb5647004c806b81d4aa6507307700a9e46dc33b3d3d15c7aa79fcdaef7848344b637c2c173de0b3f085f97a88c18e9aa755d2989f4be01d55e234c39dfe834e193b65976e4d82bd8039df8515a50833683db2289e67 
e = 65537
c = 0x502c9f367b231c49a36ed5353f9afdcc4ed7c262f593995085ab44e017c3ebb912fa94b7b06213bb9cb9ea052bdb70af922b54617a035c82be819e7f4209e5718901688be800669247a449ea8bd6f8328090396117ae6b3a292eb4f1de1806f81442d7641d35c68bd32d44f21fe36a1128bbc84258904619f749e2692b8bca
def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g 


p = (brent(num))
q = gmpy.divexact(num,p)

print(p)
print((q))


phin = (p-1) * (q-1)
d = gmpy.invert(e,phin)
print(d)

y = pow(c,d,num)
print()
print()
print(y)
print()
