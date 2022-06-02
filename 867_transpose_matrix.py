
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [[row[col_ind] for row in matrix] for col_ind in range(len(matrix[0])) ]
            

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6]]
    sol = Solution()
    res = sol.transpose(matrix)
    print(f'Result --> {res}')
    