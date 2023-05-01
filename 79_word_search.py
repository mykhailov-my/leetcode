

class Solution:
    """
    Status -> Solved with hint

    Time complexity -> O(N^3)
    Space complexity -> O(W)

    Solution
    1. iterate by each cell in matrix, if a letter is exact as first letter in a word -> run DFS
        2. check if three pointer (row, col, letter) are in bound and current letter is from word. If no -> return False
        3. check if we reached end of the word. if yes -> return true, word exist
        4. store letter of the grid (We do it so this letter won't be used in next iterations. but we need to restore it for future dfs branches)
        5. run dfs in 4 sides, if any return true -> return true
        6. restore letter in the grid

    Notes 
    """
    def exist(self, board: list[list[str]], word: str) -> bool:

        def dfs(row, col, letter=0):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and letter < len(word) and board[row][col] == word[letter]:
                letter += 1
                if letter == len(word):
                    return True
                val = board[row][col]
                board[row][col] = None
                if any((dfs(row+1, col, letter), dfs(row-1, col, letter), dfs(row, col+1, letter), dfs(row, col-1, letter))):
                    return True
                board[row][col] = val
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True
        return False


if __name__ == '__main__':
    # board = [
    #     ["C","A","A"],
    #     ["A","A","A"],
    #     ["B","C","D"]]
    # word = "AAB"
    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    word = "ABCESEEEFS"
    sol = Solution()
    res = sol.exist(board, word)
    print(f'Result --> {res}')