class Solution:

    def is_valid_range(self, row: list[str]) -> bool:
        l = list(filter(lambda x: x != '.', row))
        return len(l) == len(set(l))

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        squares = [[], [], []]
        for row in board:
            if not self.is_valid_range(row):
                return False
            squares[0].extend(row[:3])
            squares[1].extend(row[3:6])
            squares[2].extend(row[6:])
            if len(squares[0]) == 9:
                if not all([self.is_valid_range(square) for square in squares]):
                    return False
                squares = [[], [], []]
        for col_ind in range(9):
            if not self.is_valid_range([row[col_ind] for row in board]):
                return False
        return True


if __name__ == '__main__':
    t = [[".", ".", ".", ".", ".", ".", "5", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", "3", ".", ".", "2", ".", "4", ".", "."],
         [".", ".", "7", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "3", "4", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "."],
         [".", ".", ".", ".", ".", "5", "2", ".", "."]]

    sol = Solution()
    res = sol.isValidSudoku(t)
    print(f'Result --> {res}')