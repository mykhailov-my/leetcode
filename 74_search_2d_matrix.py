
from bisect import bisect_left


class Solution:
    """
    Status -> Solved by myself

    Tags -> Binary Search

    Time complexity -> O(2LogN) -> O(log N)
    Space complexity -> O(1)

    Solution
    1. if target out of min and max of matrix -> return false (min is matrix [0][0], max is matrix[-1][-1]) -> element not present in matrix
    2. find a row by biselect_left of max in row
    3. if row out right border or out of left -> return false
    4. bi_search row 
    5. if index out of row or matrix[ind] not equal to target -> return false
    6. else -> return True

    Notes 
    """
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target: #if target out of min and max of matrix -> return false
            return False
        row = bisect_left([m[-1] for m in matrix], target)
        if row == len(matrix) or (row == 0 and matrix[row][0] > target):
            return False
        else:
            ind = bisect_left(matrix[row], target)
            if ind >= len(matrix[row]) or matrix[row][ind] != target:
                return False
            else:
                return True



if __name__ == '__main__':
    n = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    t = 3 # true
    n = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    t = 13 # false
    sol = Solution()
    res = sol.searchMatrix(n, t)
    print(f'Result --> {res}')  