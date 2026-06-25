class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l=[]
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] < 0:
                    l.append(grid[i][j])
                
            
        return len(l)
