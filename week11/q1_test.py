def place_tiles(n, k):
	"""Places k tiles on an n x n grid.

	Args:
		n: The number of rows in the grid.
		k: The number of tiles to place.

	Returns:
		A list of the positions of the placed tiles.
"""

	# Initialize the list of placed tiles.
	placed_tiles = []

	# Iterate over the rows of the grid.
	for row in range(n):
		# Iterate over the columns of the grid.
		for col in range(n):
			# If the current tile is not already placed, place it.
			if (row + col) % 2 == k % 2:
				placed_tiles.append((row, col))

	return placed_tiles


def find_max_sum(grid, k, n):
	"""Finds the maximum sum of the values of the grid squares on which the tiles are placed when all k tiles are placed without overlapping.

	Args:
		grid: The grid of land values.
		k: The number of tiles to place.

	Returns:
		The maximum sum of the values of the grid squares on which the tiles are placed.
"""

	# If k is greater than the number of tiles that can be placed, return -1.
	if k > n * (n - 1) // 2:
		return -1

	# Find the maximum sum of the values of the grid squares on which the tiles can be placed.
	max_sum = 0
	for row in range(n):
		for col in range(n):
			# If the current tile is not already placed, place it.
			if (row + col) % 2 == k % 2:
				# Update the maximum sum.
				max_sum = max(max_sum, grid[row][col] + grid[row + 1][col] + grid[row + 2][col])

	return max_sum


def main():
	# Read the input.
	n, k = map(int, input().split())
	grid = []
	for _ in range(n):
		grid.append(list(map(int, input().split())))

	# Find the maximum sum of the values of the grid squares on which the tiles are placed.
	max_sum = find_max_sum(grid, k, n)

	# Print the maximum sum.
	print(max_sum)


if __name__ == "__main__":
	main()
