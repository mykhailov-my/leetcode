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
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def one_set(ind):
            result.append([nums[ind]])
            for n in nums[ind:]:
                result.append([nums[ind]])



if __name__ == '__main__':
    n = [1,2,3]
    sol = Solution()
    res = sol.subsets(n)
    print(f'Result --> {res}')  