"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity -> O(log N)
Space complexity -> O(1)

Solution
1. use python bisect module
2. get left border
3. if left more then nums or nums[left] not a target -> [-1,-1]
4. get right border, starting from left position
5. return [left, right - 1]
"""

import bisect


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, bisect.bisect_right(nums, target, left) -1]



if __name__ == '__main__':
    n = [5,7,7,8,8,10]
    t = 6
    sol = Solution()
    res = sol.searchRange(n, t)
    print(f'Result --> {res}')  