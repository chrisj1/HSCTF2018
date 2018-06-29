from itertools import combinations
from random import randint
from math import sqrt
from scipy.spatial import ConvexHull
import gmpy2
from gmpy2 import mpfr

f = open("points.txt", "r").read().splitlines()

A = []
for i in range(0,len(f)):
	splitted = f[i].split(" ")
	x = float(splitted[0])
	y = float(splitted[1])
	pnt = [x,y]
	A.append(pnt)

print(len(A))
hull = ConvexHull(A)


maxsq = 0
dx_max = 0
dy_max = 0
hull_vertices_coordinates = [hull.points[vertex] for vertex in hull.vertices]
print(hull_vertices_coordinates)

for i in range(0, len(hull_vertices_coordinates)):
	for j in range(i, len(hull_vertices_coordinates)):
		x1 = hull_vertices_coordinates[i][0]
		y1 = hull_vertices_coordinates[i][1]

		x2 = hull_vertices_coordinates[j][0]
		y2 = hull_vertices_coordinates[j][1]

		sqrtdist = (mpfr(x1-x2))**2 + (mpfr(y1-y2))**2
		if sqrtdist > maxsq:
			maxsq = sqrtdist
			dx_max = abs(x1-x2)
			dy_max = abs(y1-y2)
print(dx_max,dy_max)
print(maxsq * mpfr(10**8))