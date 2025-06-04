def findAllPath(graph, start,end, path=[]):
    path.append(start)
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPath(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


graph = {'A':['B'],
         'B':['C'],
         'C':['E','F'],
         'F':['G'],'E':['G'],
         'G':['H']}
allpath= findAllPath(graph,'A','H',[])
print(allpath)