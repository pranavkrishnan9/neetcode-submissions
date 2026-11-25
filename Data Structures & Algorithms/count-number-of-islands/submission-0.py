class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = mxn matrix grid consisting of string vals "1" or "0" where "1" represents land and "0" represents water
        #output = the number of islands (formed by connecting adjacent lands horizontally or vertically) 

        #set bounds
        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0' or (r, c) in visited: 
                return
            visited.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands+=1
                    dfs(i, j)
        
        return islands


            
            
            