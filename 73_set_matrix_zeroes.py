"""
Status -> Solved with hint

Time complexity -> O(N*M)
Space complexity -> O(1)

"""

class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:
        # use first row and column as storage
        # iterate by first column and row, if there are zeros put true to bool flag
        # iterate excluding first row and column from [1,1] to end
        # if you found zero -> place zero to first row and column
        # iterate over first row excluding first element if there a zero -> put zeros to column
        # iterate over first column excludin first row. if there is a zero -> put zeros to column
        # check flag to set zeros to first row/col if necessary 
        def wipe_row(row_ind):
            for i in range(len(matrix[row_ind])):
                matrix[row_ind][i] = 0

        def wipe_col(col_ind):
            for row in matrix:
                row[col_ind] = 0

        is_row_wiped = False
        is_col_wiped = False
        if matrix[0][0] == 0:
            is_row_wiped = True
            is_col_wiped = True
        else:
            for row in matrix:
                if row[0] == 0:
                    is_col_wiped = True
                    break
            for el in matrix[0]:
                if el == 0:
                    is_row_wiped = True
                    break
        for i, row in enumerate(matrix[1:], 1):
            for j, el in enumerate(row[1:], 1):
                if el == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i, col in enumerate(matrix[0][1:], 1):
            if col == 0:
                wipe_col(i)
        for i, row in enumerate(matrix[1:], 1):
            if row[0] == 0:
                wipe_row(i)
        if is_row_wiped:
            wipe_row(0)
        if is_col_wiped:
            wipe_col(0)


if __name__ == '__main__':
    n = [[0,1,2,0],
         [3,4,1,2],
         [1,3,1,5]]
    sol = Solution()
    res = sol.setZeroes(n)
    print(f'Result --> {n}')  