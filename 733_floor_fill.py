
from pprint import pprint


class Solution:
    """
    Status -> Solved with hint

    Time complexity -> O(R*C)
    Space complexity -> O(R*C)

    Solution
    1. store color at star x y
    2. if replaed color == input color -> we fill with same color so image stay the same
    3. Create recursive function with row and col inputs
        4. replace color
        5. check each side (left, right, top, bottom) if it has color that we are replacing. if yes -> run function for it's side

    Notes 
    """
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        replaced_color = image[sr][sc]
        if color == replaced_color:
            return image
        def color_cell(row, col):
            image[row][col] = color
            if row > 0 and image[row - 1][col] == replaced_color: # top
                color_cell(row-1, col)
            if row < len(image) - 1 and image[row + 1][col] == replaced_color: # bottom
                color_cell(row + 1, col)
            if col > 0 and image[row][col - 1] == replaced_color:  # left
                color_cell(row, col - 1)
            if col < len(image[row]) - 1 and image[row][col + 1] == replaced_color:  # right
                color_cell(row, col + 1)
        color_cell(sr, sc)
        return image



if __name__ == '__main__':
    i = [[1,1,1],
         [1,1,0],
         [1,0,1]]
    sr, sc = 1, 1
    color = 2
    i = [[0,0,0],[0,0,0]]
    color = 0
    sol = Solution()
    res = sol.floodFill(i, sr, sc, color)
    pprint(f'Result --> {res}')      