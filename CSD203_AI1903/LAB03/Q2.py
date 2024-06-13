import sys

class WGraph:
    def __init__(self):
        self.weight_matrix = []
        self.vertices = []
        self.n = 0

    def setWMatrix(self, b, m):
        self.weight_matrix = b
        self.n = m

    def setVertex(self,v):
        self.vertices = v

    def dijkstra(self, start):
        dist = [sys.maxsize] * self.n
        dist[start] = 0
        sptSet = [False] * self.n

        for _ in range(self.n):
            u = self.min_distance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.n):
                if (self.weight_matrix[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.weight_matrix[u][v]):
                    dist[v] = dist[u] + self.weight_matrix[u][v]

        return dist

    def min_distance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1

        for v in range(self.n):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

# Example usage
wg = WGraph()
wg.setWMatrix([[0, 10, 0, 0, 5], [0, 0, 1, 0, 2], [0, 0, 0, 4, 0], [7, 0, 6, 0, 0], [0, 3, 9, 2, 0]], 5)
wg.setVertex(['A','B','C','D','E'])
print("Dijkstra:", wg.dijkstra(0))  