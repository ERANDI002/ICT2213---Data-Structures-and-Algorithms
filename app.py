from driver_manager import DriverManager,dijkstra
from graph import Graph,MinHeap


# Ride Matching App

class RideApp:
    def __init__(self):
        self.graph = self.build_graph()
        self.drivers = DriverManager()
        self.load_drivers()

    def build_graph(self):
        g = Graph()
        # Add few locations (simplified)
        for loc in ["Fort", "Pettah", "Kollupitiya", "Bambalapitiya", "Nugegoda","Maharagama"]:
            g.add_vertex(loc)

        # Add roads
        g.add_edge("Fort", "Pettah", 2)
        g.add_edge("Fort", "Kollupitiya", 3)
        g.add_edge("Kollupitiya", "Bambalapitiya", 2)
        g.add_edge("Bambalapitiya", "Nugegoda", 5)
        g.add_edge("Maharagama","Nugegoda",7)
        return g

    def load_drivers(self):
        self.drivers.add_driver("D001", "Fort")
        self.drivers.add_driver("D002", "Kollupitiya")
        self.drivers.add_driver("D003", "Nugegoda", "Busy")
        self.drivers.add_driver("D004", "Bambalapitiya")
        self.drivers.add_driver("D005","Nugegoda")

    def request_ride(self, pickup, destination):
        print("\n=== RIDE REQUEST ===")
        print(f"Pickup: {pickup}")
        print(f"Destination: {destination}\n")

        nearby = self.drivers.find_drivers_near(pickup)
        if not nearby:
            print("❌ No available drivers found!")
            return

        driver = nearby[0]
        print(f"✓ Matched with {driver['id']} at {driver['location']}")

        path, distance = dijkstra(self.graph, pickup, destination)
        if distance == float('infinity'):
            print("❌ No route found!")
            return

        print("\n=== ROUTE DETAILS ===")
        print(f"Driver: {driver['id']}")
        print(f"Route: {' → '.join(path)}")
        print(f"Distance: {distance} km")
        print(f"Estimated Fare: LKR {int(distance * 100)}")


if __name__ == "__main__":
    app = RideApp()
    pickupLOC = input("enter pickup location: ")
    destinationLOC = input("enter destination: ")
    app.request_ride(pickupLOC,destinationLOC)

