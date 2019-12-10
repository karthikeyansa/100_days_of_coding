#string substring
n = input()
res = [n[x:y] for x in range(len(n)) for y in range(x+1,len(n)+1)]
print(str(res))
