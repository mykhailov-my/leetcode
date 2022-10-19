
class Solution:
    """
    Status -> Solved by myself

    Tags -> BFS

    Time complexity -> O(R*C)
    Space complexity -> O(R*C)

    Solution
    1. create separate function that using bfs will traverse single island and return coordinates of each land chunk
    2. traverse all coordinates one by one, if there is chunk of land and it's not in seen -> run method from step 1
        3. update max len with len of returned set, update total seen set with returned set
    4. return max

    Notes 
    """

    def traverse_island(self, row, col, grid):
        seen = {(row,col)}
        queue = [(row,col)]

        while queue:
            row, col = queue.pop()

            if row > 0 and grid[row -1][col] == 1 and (row - 1, col) not in seen: # top
                seen.add((row - 1, col))
                queue.append((row - 1, col))
            if row < len(grid) - 1 and grid[row +1][col] == 1 and (row + 1, col) not in seen: # bottom
                seen.add((row + 1, col))
                queue.append((row + 1, col))
            if col > 0 and grid[row][col -1] == 1 and (row, col - 1) not in seen:  # left
                seen.add((row, col - 1))
                queue.append((row, col - 1))
            if col < len(grid[row]) - 1 and grid[row][col + 1] == 1 and (row, col + 1) not in seen:  # right
                seen.add((row, col + 1))
                queue.append((row, col + 1))
        return seen

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        total_seen = set()
        max_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in total_seen:
                    seen = self.traverse_island(i, j, grid)
                    max_island = max(max_island, len(seen))
                    total_seen.update(seen)
        return max_island



if __name__ == '__main__':
    n = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution()
    res = sol.maxAreaOfIsland(n)
    print(f'Result --> {res}')  