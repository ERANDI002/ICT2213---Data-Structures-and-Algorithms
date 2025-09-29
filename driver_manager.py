from graph import MinHeap

# Driver Manager (Hash Map)

class DriverManager:
    def __init__(self):
        self.drivers = {}

    def add_driver(self, driver_id, location, status="Available"):
        self.drivers[driver_id] = {"id": driver_id, "location": location, "status": status}

    def find_drivers_near(self, location):
        # find drivers in same location only
        return [d for d in self.drivers.values() if d["location"] == location and d["status"] == "Available"]


# Dijkstra Algorithm

def dijkstra(graph, start, end):
    distances = {v: float('infinity') for v in graph.vertices}
    distances[start] = 0
    previous = {v: None for v in graph.vertices}

    pq = MinHeap()
    pq.push(0, start)
    visited = set()

    while not pq.is_empty():
        current_dist, current = pq.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            break

        for neighbor, weight in graph.get_neighbors(current):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                pq.push(distance, neighbor)

    # Build path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[end]