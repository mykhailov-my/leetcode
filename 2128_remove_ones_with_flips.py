"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        swapped_col = set()
        swapped_row = set()
        def swap_col(col):
            for row in grid:
                row[col] = 1 if row[col] == 0 else 0
            swapped_col.add(col)
        def swap_row(row):
            for i in range(len(grid[row])):
                grid[row][i] = 1 if grid[row][i] == 0 else 0
            swapped_row.add(row)
        
        for row in grid:
            try:
                index = row.index(1)

            except ValueError:
                pass



if __name__ == '__main__':
    n = [[0,1,0],
         [1,0,1],
         [0,1,0]]
    n = [[0,1,0],
         [1,0,1],
         [1,0,1]]
    n = [[0,1,1],
         [1,0,0],
         [0,1,1]]
    n = [[0,0,0],
         [0,1,1],
         [0,1,1]]
    sol = Solution()
    res = sol.removeOnes(n)
    print(f'Result --> {res}')  