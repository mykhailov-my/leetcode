"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""

class Solution:
    '''
    Not working for edge-case [3,2,2,2,4]
    '''
    def findDuplicate(self, nums: list[int]) -> int:
        n = max(nums)
        n_sum = ((min(nums) + n) * n) // 2
        for num in nums:
            n_sum -= num
        res = abs(n_sum) // (len(nums) - n)
        breakpoint()
        return res if res <= n else n
        pass



if __name__ == '__main__':
    n = [1,3,4,2,2,2]
    n = [2,2,2,2,2]
    n = [1,4,4,2,4]
    n = [3,2,2,2,4]
    sol = Solution()
    res = sol.findDuplicate(n)
    print(f'Result --> {res}')  