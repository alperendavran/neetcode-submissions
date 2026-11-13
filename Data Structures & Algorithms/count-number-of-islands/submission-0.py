class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] != "1" or (row, col) in visited:
                    continue

                # Yeni bir ada bulduk
                islands += 1
                stack = [(row, col)]
                visited.add((row, col))

                # Bu adanın bütün karalarını gez
                while stack:
                    r, c = stack.pop()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                stack.append((nr, nc))

        return islands