def findpath(graph,start,end,path = []):
    path.append(start)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = findpath(graph,node,end,path)
            if newpath:return newpath
        return None
graph = {'a':['c'],
         'b':['d'],
         'c':['e'],
         'd':['a','d'],
         'e':['b','c']
         }
start = str(input('enter starting vertex:'))
end = str(input('enter ending vertex:'))
print(findpath(graph,start,end))
