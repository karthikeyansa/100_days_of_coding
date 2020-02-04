n = int(input())
for i in range(1,n+1):
	m = int(input())
	l = []
	for j in range(1,m+1):
		if j % 2 != 0:
			l.append(j)
	print(l[-2])