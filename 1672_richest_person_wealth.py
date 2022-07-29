"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)


"""

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])


class Solution2:
    '''
    Time complexity -> O(N)
    Space complexity -> O(1)
    '''
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_ = 0
        for acc in accounts:
            max_ = max(sum(acc), max_)
        return max_


if __name__ == '__main__':
    n = [[1,5],[7,3],[3,5]]
    sol = Solution()
    res = sol.maximumWealth(n)
    print(f'Result --> {res}')  