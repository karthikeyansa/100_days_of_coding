string = 'github'
first =[]
strlen = len(string)
half = strlen//2
for i in range(half):
	value = ' '*(i) + string[i] + ' '*(strlen - (2) - 2*i) +string[strlen-1-i]
	first.append(value)
middle = [' '*half + string[half]]
last = first[ ::-1]
result = first + middle +last
for i in result:
	print(i)