import numpy as np

class WGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.weighted_matrix = np.zeros((num_vertices, num_vertices))
    
    def add_edge(self, u, v, weight):
        self.weighted_matrix[u][v] = weight
        self.weighted_matrix[v][u] = weight
    
    def min_spanning_tree(self):
        selected = [False] * self.num_vertices
        mst_edges = []
        edge_count = 0
        selected[0] = True
        
        while edge_count < self.num_vertices - 1:
            minimum = float('inf')
            a = b = -1
            for i in range(self.num_vertices):
                if selected[i]:
                    for j in range(self.num_vertices):
                        if not selected[j] and self.weighted_matrix[i][j]:
                            if minimum > self.weighted_matrix[i][j]:
                                minimum = self.weighted_matrix[i][j]
                                a, b = i, j
            selected[b] = True
            edge_count += 1
            mst_edges.append((a, b, self.weighted_matrix[a][b]))
        
        return mst_edges

# Example usage
wg = WGraph(5)
wg.add_edge(0, 1, 2)
wg.add_edge(0, 3, 6)
wg.add_edge(1, 2, 3)
wg.add_edge(1, 3, 8)
wg.add_edge(1, 4, 5)
wg.add_edge(2, 4, 7)
wg.add_edge(3, 4, 9)

mst = wg.min_spanning_tree()
print("Edges in the minimum spanning tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")