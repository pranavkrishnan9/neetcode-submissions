class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = 2x2 grid where '1' represents land and '0' represents water
        #output = number of islands

        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == '0':
                return;
            
            visited.add((r,c))

            dfs(r-1,c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        
        return islands
