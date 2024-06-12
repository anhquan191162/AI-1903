import sys

class WeightedGraph:
    def __init__(self):
        self.weight_matrix = []
        self.n = 0
    def setMatrix(self,b,m):
        self.weight_matrix = b
        self.n = m
    