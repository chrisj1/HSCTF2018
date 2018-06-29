from itertools import combinations
from random import randint

A = [[randint(-5,5) for coord in range(2)] for point in range(500)]
print(A)

def square_distance(x,y): return sum([(xi-yi)**2 for xi, yi in zip(x,y)])    

max_square_distance = 0
for pair in combinations(A,2):
    if square_distance(*pair) > max_square_distance:
        max_square_distance = square_distance(*pair)
        max_pair = pair