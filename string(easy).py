def fun(s,l,leng,count):
	lis = []
	x = 0
	y = l
	for i in range(1,slen+1):
		res = s[x:y]
		if count != 0:
			lis.append(res)
		else:
			return lis
		x += 1
		y += 1
		count -= 1#return none for single value
def flattenList(lis2):
    results = []
    for rec in lis2:
        if isinstance(rec, list):
            results.extend(rec)
            results = flattenList(results)
        else:
            results.append(rec)
    return results #convert nested list to single
s = input()
slen = len(s)
lis = []
l = 1
count = len(s)
for word in s:
	lis.append(word)
for i in range(1,slen+1):
	val = fun(s,l,slen,count)
	lis.append(val)
	count -= 1
	l += 1
lis2 = []
for j in lis:
	lis2.append(j)
res = flattenList(lis2)
out = []
for item in res:#to remove None
	if item != None:
		out.append(item)
print(out)