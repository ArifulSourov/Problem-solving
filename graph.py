# Python program to generate shortest path 
  
graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
} 
  
# function to find the shortest path 
def find_shortest_path(graph, start, end, path =[]): 
        path = path + [start] 
        if start == end: 
            return path 
        shortest = None
        for node in graph[start]: 
            if node not in path: 
                newpath = find_shortest_path(graph, node, end, path) 
                if newpath: 
                    if not shortest or len(newpath) < len(shortest): 
                        shortest = newpath 
        return shortest 
          
# Driver function call to print 
# the shortest path 
print(find_shortest_path(graph, 'd', 'c')) 
