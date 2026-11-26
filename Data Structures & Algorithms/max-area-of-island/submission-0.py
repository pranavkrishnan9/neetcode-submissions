class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #input = grid[][] where grid[i] is either a 0 (water) or 1 (land).
        #Key Note: An island is defined as a group of 1s connected horizontally or vertically
        #output = the max area of an island in grid (with an island being defined as above), so essentially the island with the most 1s

        #will contain tuples of grid coords visited
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r, c))

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea


        