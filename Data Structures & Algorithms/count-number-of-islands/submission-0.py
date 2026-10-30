class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])
        island = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()

        def bfs(r,c):
            q = deque()
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if ((nr in range(rows)) and (nc in range(cols)) and ((nr, nc) not in visit) and (grid[nr][nc] == "1")):
                        q.append((nr, nc))
                        visit.add((nr, nc))

                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    island += 1

        return island




