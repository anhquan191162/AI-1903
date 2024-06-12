def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
    return adj
def DFSUtil(u,adj,visited):
    visited[u] = True
    print(u,end=' ')
    for i in range(len(adj[u])):
        if (visited[adj[u][i]]==False):
            DFSUtil(adj[u][i],adj,visited)
def DFS(adj,V):
    visited = [False]*(V+1)
    for u in range(V):
        if (visited[u]==False):
            DFSUtil(u,adj,visited)

if __name__ == '__main__':
    V = 5
    adj = [[] for i in range(V)]

    adj = addEdge(adj,0,1)
    adj = addEdge(adj,0,4)
    adj = addEdge(adj, 1, 2)
    adj = addEdge(adj, 1, 3)
    adj = addEdge(adj, 1, 4)
    adj = addEdge(adj, 2, 3)
    adj = addEdge(adj, 3, 4)
    DFS(adj, V) 