import heapq

# Graph (Road Network)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, location):
        if location not in self.vertices:
            self.vertices[location] = []

    def add_edge(self, src, dest, distance):
        self.vertices[src].append((dest, distance))
        self.vertices[dest].append((src, distance))  # Undirected

    def get_neighbors(self, location):
        return self.vertices.get(location, [])



# MinHeap (for Dijkstra)
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, distance, location):
        heapq.heappush(self.heap, (distance, location))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


