def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    :param grid: List[List[int]] - 2D list representing the grid
    :return: int - perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Start with 4 sides for each land cell

                # Check if the cell has neighboring land cells and adjust the perimeter
                if r > 0 and grid[r - 1][c] == 1:  # Top
                    perimeter -= 2  # Remove 2 sides

                if c > 0 and grid[r][c - 1] == 1:  # Left
                    perimeter -= 2  # Remove 2 sides

    return perimeter
