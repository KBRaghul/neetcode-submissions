class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        island = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        def dfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if ((nr in range(rows)) and (nc in range(cols)) and (grid[nr][nc] == "1") and ((nr, nc) not in visited)):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    dfs(r, c)
                    visited.add((r,c))
                    island += 1
                
        

        return island
