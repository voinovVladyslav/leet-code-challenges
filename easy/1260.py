def shiftGrid(grid: list[list[int]], k: int) -> list[list[int]]:
    m = len(grid)

    for i in range(k):
        for i in range(m-1):
            prev = grid[i][-1]
            grid[i].pop(-1)
            grid[i+1].insert(0, prev)

        grid[0].insert(0, grid[-1][-1])
        grid[-1].pop(-1)
    
    return grid

g = shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9)

for i in g:
    print(i)