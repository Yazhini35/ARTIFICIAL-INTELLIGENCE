import itertools

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

# Function to calculate total distance of a path
def total_distance(path, cities):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(cities[path[i]], cities[path[i + 1]])
    dist += distance(cities[path[-1]], cities[path[0]])  # Return to starting point
    return dist

# Function to solve TSP using brute force
def tsp_brute_force(cities):
    num_cities = len(cities)
    shortest_distance = float('inf')
    shortest_path = None

    # Generate all permutations of cities
    for perm in itertools.permutations(range(num_cities)):
        dist = total_distance(perm, cities)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_path = perm

    return shortest_path, shortest_distance

# Example usage
if __name__ == "__main__":
    # Example cities represented as (x, y) coordinates
    cities = [(0, 0), (1, 2), (3, 1), (5, 3)]

    shortest_path, shortest_distance = tsp_brute_force(cities)

    print("Shortest path:", shortest_path)
    print("Shortest distance:", shortest_distance)
