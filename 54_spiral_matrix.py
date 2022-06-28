"""
Status -> Implemented with solution

Time complexity -> O(n*m)
Space complexity -> O(n*m)

Solution
1.
2.
3.
"""

class Solution:
    # This solution don't cover some edge cases
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        i = 0
        while i <= len(matrix) // 2:

            if i != len(matrix) -1:
                top = matrix[i][i: len(matrix[i]) -i]
                result.extend(top)
            
            right = [row[len(row) -1 -i] for row in matrix[i + 1:len(matrix) -1 -i]]
            result.extend(right)

            if i != len(matrix) // 2:
                bottom = matrix[len(matrix) -1 -i][i:len(matrix[i]) -i][::-1]
                result.extend(bottom)
            
            if i + 1 != len(matrix[0]):
                left = [row[i] for row in matrix[i + 1:len(matrix) -1 -i]][::-1]
                result.extend(left)
            breakpoint()
            i+=1

            # print(result)
        return result

class BestSolution:
    """
    Time Complexity -> O(N*M)
    Space complexity -> O(N*M)
    """
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

if __name__ == '__main__':
    # n = [[1 ,2 ,3 ,4 ],
    #      [5 ,6 ,7 ,8 ],
    #      [9 ,10,11,12]]
    n = [[2,5,8],
         [4,0,-1]]
    # n = [[1]]
    # n = [[1, 2, 3, 4, 5 ],
    #      [6, 7, 8, 9, 10],
    #      [11,12,13,14,15],
    #      [16,17,18,19,20],
    #      [21,22,23,24,25]]
    sol = BestSolution()
    res = sol.spiralOrder(n)
    print(f'Result --> {res}')  