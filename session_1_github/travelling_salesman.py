import itertools
import math

def calculate_distance(city1, city2):
	"""Calculate Euclidean distance between two cities."""
	return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def traveling_salesman_brute_force(cities):
	"""
	Solve TSP using brute force approach.
	
	Args:
		cities: List of tuples representing (x, y) coordinates of cities
	
	Returns:
		Tuple of (shortest_distance, best_path)
	"""
	n = len(cities)
	if n < 2:
		return 0, cities
	
	# Generate all possible permutations starting from first city
	min_distance = float('inf')
	best_path = None
	
	# Fix the first city and permute the rest
	for perm in itertools.permutations(range(1, n)):
		path = [0] + list(perm) + [0]  # Return to starting city
		distance = 0
		
		for i in range(len(path) - 1):
			distance += calculate_distance(cities[path[i]], cities[path[i + 1]])
		
		if distance < min_distance:
			min_distance = distance
			best_path = path
	
	return min_distance, best_path

def traveling_salesman_nearest_neighbor(cities):
	"""
	Solve TSP using nearest neighbor heuristic.
	
	Args:
		cities: List of tuples representing (x, y) coordinates of cities
	
	Returns:
		Tuple of (total_distance, path)
	"""
	n = len(cities)
	if n < 2:
		return 0, list(range(n))
	
	unvisited = set(range(1, n))
	current_city = 0
	path = [current_city]
	total_distance = 0
	
	while unvisited:
		nearest_city = min(unvisited, 
						  key=lambda city: calculate_distance(cities[current_city], cities[city]))
		
		total_distance += calculate_distance(cities[current_city], cities[nearest_city])
		current_city = nearest_city
		path.append(current_city)
		unvisited.remove(current_city)
	
	# Return to starting city
	total_distance += calculate_distance(cities[current_city], cities[0])
	path.append(0)
	
	return total_distance, path

# Example usage
if __name__ == "__main__":
	# Example cities with (x, y) coordinates
	cities = [(0, 0), (1, 2), (3, 1), (5, 3), (2, 4)]
	
	print("Cities:", cities)
	
	# Brute force solution (optimal but slow for large inputs)
	if len(cities) <= 8:  # Only use brute force for small inputs
		distance, path = traveling_salesman_brute_force(cities)
		print(f"\nBrute Force Solution:")
		print(f"Shortest distance: {distance:.2f}")
		print(f"Best path: {path}")
	
	# Nearest neighbor heuristic (faster but approximate)
	distance_nn, path_nn = traveling_salesman_nearest_neighbor(cities)
	print(f"\nNearest Neighbor Solution:")
	print(f"Distance: {distance_nn:.2f}")
	print(f"Path: {path_nn}")