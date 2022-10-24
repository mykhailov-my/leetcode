
from collections import deque



class Solution:
    """
    Status -> Implemented with solution

    Tags -> BFS

    Time complexity -> O(R*C)
    Space complexity -> O(R*C)

    Solution
    1. Iterate over matrix, count fresh oranges and add to queue rotten
    2. add to queue separator (-1)
    3. go bfs
        4. when populate from queue check separtor (-1) and if it's a separator it means we done with iteration
        so increment timer, and if smth left in equry add new separator
    5. return timer if no fresh oranges else -1

    Notes 
    """

    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        oranges_counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    oranges_counter += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        queue.append((-1, -1))

        minutes = -1
        directions = ((1,0), (0, 1), (-1, 0), (0, -1))
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    adjacent_row, adjacent_col = row + d[0], col + d[1]
                    if len(grid) > adjacent_row >= 0 and len(grid[row]) > adjacent_col >= 0:
                        if grid[adjacent_row][adjacent_col] == 1:
                            grid[adjacent_row][adjacent_col] = 2
                            oranges_counter -= 1
                            queue.append((adjacent_row, adjacent_col))
        
        return minutes if oranges_counter == 0 else -1


if __name__ == '__main__':
    n = [[2,1,1],
         [1,1,0],
         [0,1,1]] # 4

    sol = Solution()
    res = sol.orangesRotting(n)
    print(f'Result --> {res}')  