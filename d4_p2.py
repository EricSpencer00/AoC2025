# find the amount of rolls can be accessed by forklifts
with open('inputs/d4_input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

def find_x():
    # define the first character
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    total_accessible = 0

    while True:
        accessible_positions = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    # check adjacent positions
                    adjacent_positions = [
                        (r-1, c-1), (r-1, c), (r-1, c+1),
                        (r, c-1),               (r, c+1),
                        (r+1, c-1), (r+1, c), (r+1, c+1)
                    ]
                    adjacent_count = 0
                    for ar, ac in adjacent_positions:
                        if 0 <= ar < rows and 0 <= ac < cols:
                            if grid[ar][ac] == '@':
                                adjacent_count += 1
                    if adjacent_count < 4:
                        accessible_positions.append((r, c))

        if not accessible_positions:
            break

        for r, c in accessible_positions:
            grid[r][c] = '.'
        total_accessible += len(accessible_positions)

    return total_accessible

result = find_x()
print(result)