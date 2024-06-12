class Vertex:
    def __init__(self,x):
        self.data = x
    def element(self):
        return self.data
    def __hash__(self):
        return hash(id(self))
class Edge:
    def __init__(self,u,v,x):
        self.origin = u
        self.destination = v
        self.data = x
    def endpoints(self):
        return (self.origin,self.destination)
    def opposite(self,v):
        return self.destination if v is self.origin else self.origin
    def element(self):
        return self.data
    def __hash__(self):
        return hash((self.origin,self.destination))
class Graph:
    def __init__(self,directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    def is_directed(self):
        return self._incoming is not self._outgoing
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    def edge_count(self):
        total = sum((len(self._outgoing[v] for v in self._outgoing)))
        return total if self.is_directed() else total // 2
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    def get_edges(self,u,v):
        return self._outgoing[u].get(v)
    def degree(self,v,outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self,v,outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    def insert_edge(self,u,v,x=None):
        e = Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
    