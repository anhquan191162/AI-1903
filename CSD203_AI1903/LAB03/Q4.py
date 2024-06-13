import numpy as np
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1
    
    def sequential_coloring(self):
        result = [-1] * self.num_vertices
        result[0] = 0
        
        available = [True] * self.num_vertices
        
        for u in range(1, self.num_vertices):
            for i in range(self.num_vertices):
                if self.adjacency_matrix[u][i] == 1 and result[i] != -1:
                    available[result[i]] = False
            
            cr = 0
            while cr < self.num_vertices:
                if available[cr]:
                    break
                cr += 1
            
            result[u] = cr
            
            available = [True] * self.num_vertices
        
        return result

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

colors = g.sequential_coloring()
print("Vertex colors:")
for vertex, color in enumerate(colors):
    print(f"Vertex {vertex}: Color {color}")