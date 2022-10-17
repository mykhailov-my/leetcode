from random import randint


class Solution:
    """
    Status -> Solved with hint

    Time complexity -> 
    Space complexity -> 

    Solution
    1. store color at star x y
    2. if replaed color == input color -> we fill with same color so image stay the same
    3. Create recursive function with row and col inputs
        4. replace color
        5. check each side (left, right, top, bottom) if it has color that we are replacing. if yes -> run function for it's side

    Notes 
    """
    def get_start_position(self, grid):
        r,c = 0, 0
        while grid[r][c] != 1:
            r, c = randint(0, len(grid) - 1), randint(0, len(grid[0]) - 1)
        return r,c
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        r, c = self.get_start_position(grid)
        perimetr = 0
        def traverse_land(row, col, origin):
            perimetr = 0
            # print(f'ROW {row} COL {col}')
            if origin != 'top':
                if row > 0 and grid[row -1][col] == 1: # top
                    perimetr += traverse_land(row-1, col, 'bot')
                else:
                    perimetr += 1
            if origin != 'bot':
                if row < len(grid) - 1 and grid[row +1][col] == 1: # bottom
                    perimetr += traverse_land(row + 1, col, 'top')
                else:
                    perimetr += 1
            if origin != 'left':
                if col > 0 and grid[row][col -1] == 1:  # left
                    perimetr += traverse_land(row, col - 1, 'right')
                else:
                    perimetr += 1
            if origin != 'right':
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:  # right
                    perimetr += traverse_land(row, col + 1, 'left')
                else:
                    perimetr += 1
            return perimetr
        perimetr = traverse_land(r,c, '')
        return perimetr




if __name__ == '__main__':
    n = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    sol = Solution()
    res = sol.islandPerimeter(n)
    print(f'Result --> {res}')      