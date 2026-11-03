def all_explode(grid):
    def explode(coord):
        r, c = coord
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 'exploded':
            return
        paths = []
        if grid[r][c] == '+':
            paths.extend([(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)])
        elif grid[r][c] == 'x':
            paths.extend([(r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)])
        grid[r][c] = 'exploded'
        for path in paths:
            explode(path)
    explode((0, 0))
    return not any(element in ['+', 'x'] for row in grid for element in row)

print(all_explode([
  ["+", "+", "0", "x", "x", "+", "0"],
  ["0", "+", "+", "x", "0", "+", "x"]
])== False)

print(all_explode([
  ["x", "0", "0"],
  ["0", "0", "0"],
  ["0", "0", "x"]
])== False) 

print(all_explode([
  ["x", "0", "x"],
  ["0", "x", "0"],
  ["x", "0", "x"]
])== True)

print(all_explode([
  ["+", "+", "+", "+", "+", "+", "x"]
])== True)

print(all_explode([
  ["+", "+", "+", "+", "+", "0", "x"]
])== False)