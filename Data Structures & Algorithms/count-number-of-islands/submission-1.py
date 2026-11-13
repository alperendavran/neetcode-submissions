class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        islands = 0 

        directions = [(0,1), (0,-1), (1,0), (-1,0) ]

        for row in range(rows):
            for col in range(columns):

                if grid[row][col] != "1" or (row,col) in visited: 
                    continue

                islands += 1

                stack = [(row, col)]
                visited.add((row,col))

                while(stack):
                    r , c = stack.pop()  
                    for x,y in directions:
                        nr = r + x 
                        nc = c + y 

                        if 0 <= nr < rows and 0 <=  nc < columns:
                            if grid[nr][nc] == "1" and (nr,nc) not in visited:
                                visited.add((nr,nc))
                                stack.append((nr,nc))


        return islands

              

