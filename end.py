f = open("end.txt", "r")

strings = f.read().splitlines()

data = []
for string in strings:
	line = string.split(" ")[:-1]
	line_array = []
	for t in line:
		line_array.append(int(t))
	data.append(line_array)

new = []
for i in range(0, 5000):
	new.append([0] * 5000)
print("calculate")
for y in range(4999, -1, -1):
	for x in range(0,5000):
		x_left = 0
		if x != 0:
			x_left = new[x-1][y]
		y_down = 0
		if y != 4999:
			y_down = new[x][y+1]
		new[x][y] = x_left + y_down
		if data[x][y] == 1:
			new[x][y] = 0
		if x == 0 and y == 4999:
			new[x][y] = 1

	print(y)
	
print(new[4999][0]%(10**9 + 7))
print("done")