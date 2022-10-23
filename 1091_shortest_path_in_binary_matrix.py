
from collections import deque


class Solution:
    """
    Status -> Solved by myself

    Tags -> BFS

    Time complexity ->
    Space complexity ->

    Solution
    1. Validation of input (if start pos is 1 or if it's just one cell)
    2. At this point use bfs, but seen is not a set but a dict (row, col) -> path
    3.

    Notes 
    """
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1

        query = deque()
        query.append((0, 0))
        seen = {(0, 0): 1}

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1))
        # min_path = float('inf')
        while query:
            # print(query)
            row, col = query.popleft()
            for d in directions:
                adjacent_row, adjacent_col = row + d[0], col + d[1]
                if len(grid) > adjacent_row >= 0 and len(grid[row]) > adjacent_col >= 0 and (adjacent_row, adjacent_col) not in seen:
                    if grid[adjacent_row][adjacent_col] == 0:
                        if adjacent_row == len(grid) -1 and adjacent_col == len(grid[row]) -1:
                            return seen[(row, col)] + 1
                            # return min(seen[(row, col)] + 1, min_path)
                        else:
                            seen[(adjacent_row, adjacent_col)] = seen[(row, col)] + 1
                            query.append((adjacent_row, adjacent_col))

        return -1
        # return min_path if min_path != float('inf') else -1




if __name__ == '__main__':
    n = [[0,1],[1,0]] # 2
    n = [[0,0,0],[1,1,0],[1,1,0]]  # 4
    n = [[0, 0]]
    # n = [[0,0,0],
    #      [1,1,1],
    #      [1,1,0]] # -1
    # n = [[0,0,0],
    #      [0,1,0],
    #      [0,0,0]]  # 4
    n = [[0,1,0,1,0],
         [1,0,0,0,1],
         [0,0,1,1,1],
         [0,0,0,0,0],
         [1,0,1,0,0]] # 6
    sol = Solution()
    res = sol.shortestPathBinaryMatrix(n)
    print(f'Result --> {res}')  