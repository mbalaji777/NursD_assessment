def depthFirstSearch(s) : 
  #path contains all the nodes starting from the node that has zero in-degree
  path.append(s)
  #visited is a marker which contains the nodes that are visited, and nodes that are unvisited
  visited[s] = True
  
  #if the node does not have a outdegree, and the first node does not have an indegree, then the path is complete
  if outDegreeZero[s] and inDegreeZero[path[0]] :
    print(*path)
  
  #if the nodes have an adjacent node, the DFS is possible and the node is not visited, then recur using depthFirstSearch function
  for nodes in adjacentNode[s] : 
    if not visited[nodes] : 
      depthFirstSearch(nodes)
  #pop the nodes that has shown path, and reset the visited node to false
  path.pop()
  visited[s] = False
#function to find all the possible paths using DFS
def findAllPaths(n) : 
  for i in range(0, n) : 
    if inDegreeZero[i] and adjacentNode[i] : 
      path = []
      visited = [False] * (n+1)
      depthFirstSearch(i)

#Getting the number of nodes as an integer and edges as strings. 
n = int(input())
edges = list()
for i in range(0, n - 1) : 
  x = input()
  tempList = list(map(int, x.split(',')))
  edges.append(tempList)

from collections import defaultdict
# set all nodes unvisited 
visited = [False] * (n + 1) 
path = [] 
adjacentNode = defaultdict(list)
inDegreeZero = [True] * n
outDegreeZero = [True] * n 
for x in edges : 
  u, v = x[0], x[1]
  adjacentNode[u].append(v)
  inDegreeZero[v] = False
  outDegreeZero[u] = False
#Printing the nodes with zero in-degree
for i in range(0, n) : 
  if inDegreeZero[i] == True : 
    print("The", i, "th node has zero in-degree")

#code for finding all possible paths
findAllPaths(n)

