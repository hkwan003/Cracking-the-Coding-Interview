from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices   #No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def isReachable(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Create a queue for BFS
        queue = []
        # Mark the source code as visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            print("Queue: ", queue)
            # Dequeue a vertex from queue
            n = queue.pop(0)
            # If this adjacent node is the destination node, then return True
            if n == d:
                return True
            # else continue doing BFS
            for i in self.graph[n]:
                print("I: ", i)
                if not visited[i]:
                    queue.append(i)
                    print("Visited: ", visited)
                    visited[i] = True
        # If BFS is complete without visited D
        return False
g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
u = 1
v = 3
if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))
# u = 3
# v = 1
# if g.isReachable(u, v):
#     print("There is a path from %d to %d" % (u, v))
# else:
#     print("There is no path from %d to %d" % (u, v))