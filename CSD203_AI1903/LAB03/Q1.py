def write_matrix_to_file(filename, matrix):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')
def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.strip().split())) for line in f]
    return matrix
matrix =    [

     #A  B  C  D  E  F  G  H  I
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0]      
            
            
            ]
            
write_matrix_to_file('adjacency.txt',matrix)
read_matrix = read_matrix_from_file('adjacency.txt')
class Graph:
    def __init__(self):
        self.adjacency = []
        self.vertices = []
        self.n = 0

    def setMatrix(self,filename):
        self.adjacency = read_matrix_from_file(filename)
        self.n = len(self.adjacency)
    def setVertices(self,v):
        self.vertices = v
    def bfs(self,starting_v):
        visited = [False] *self.n
        queue = []
        res = []
        queue.append(starting_v)
        visited[starting_v] = True
        while queue:
            vertex = queue.pop(0)
            res.append(self.vertices[vertex])
            
            for i in range(self.n):
                if self.adjacency[vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return res
    def dfs(self,starting_v):
        visited = [False]*self.n
        stack = []
        res = []
        stack.append(starting_v)
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                res.append(self.vertices[vertex])
                visited[vertex] = True
            for i in range(self.n -1,-1,-1):
                if self.adjacency[vertex][i] == 1 and not visited[i]:
                    stack.append(i)
        return res


g = Graph()
g.setMatrix('adjacency.txt')
g.setVertices(['A', 'B', 'C', 'D', 'E','F','G','H','I'])

print("BFS:", g.bfs(0)) 
print("DFS:", g.dfs(0))  