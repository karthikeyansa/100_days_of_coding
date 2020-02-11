n = 5
for i in range(n):
	print((' *'*i).center(7))
l=[]
for j in range(n):
	c = ('* '*j).center(10)
	l.append(c)
l.reverse()
print(*l,sep='\n')