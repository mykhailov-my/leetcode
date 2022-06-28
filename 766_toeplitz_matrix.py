"""
Status -> Implemented with solution

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
[2][0]
[1][0] [2][1]
[0][0] [1][1] [2][2]
[0][1] [1][2] [1][3]
[0][2] [1][3]
[0][3]
"""


class Solution:
    # Not working

    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        top_i = len(matrix) - 1
        top_j = 0
        while top_i >= 0 and top_j < len(matrix[0]):
            print(f'TOP {matrix[top_i][top_j]}')
            for i in range(top_i, len(matrix) - 1):
                for j in range(top_j, len(matrix[0])):
                    if matrix[top_i][top_j] != matrix[i][j]:
                        breakpoint()
                        return False
            if top_i - 1 >= 0:
                top_i -= 1
                if top_i == 0 and top_j == 0:
                    top_j -= 1
            if top_i == 0:
                top_j += 1
        return True


class BestSolution:
    '''
    Solution
    1. loop by matrix, loop by row
    2 if it's a first row or first column -> they valid as it's
    3 if current val == to top left value (it's always be top left value cos we skip if they are first) all good

    Time complexity -> O(n*m)
    Space complexity -> O(1)
    '''

    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val 
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))


if __name__ == '__main__':
    n = [[1, 2, 3, 4],
         [5, 1, 2, 3],
         [9, 5, 1, 2]]
    sol = BestSolution()
    res = sol.isToeplitzMatrix(n)
    print(f'Result --> {res}')
