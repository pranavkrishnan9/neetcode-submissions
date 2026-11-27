class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = 2x2 grid where '1' represents land and '0' represents water
        #return number of islands
        islands = 0
        #identify bounds for grid iteration
        rows, cols = len(grid), len(grid[0])
        #identify visited cells with a set so they aren't revisited
        visited = set()
        #define dfs method
        def dfs(r,c):
            if r < 0 or c < 0  or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0' or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
            

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands