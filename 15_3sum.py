"""
Status -> Implemented with solution

Time complexity ->
Space complexity ->

Solution
1. initate hash map for result, duplicates for val1 and dict seen
2. iterate by nums for first value
3. if first value not in duplicates hash ->
4. add value to duplicates
5. Iterate by nums starting from next position from val1
6. complement = -val1 - val2 (v1 + v2 + v3 = 0| -v3 = v1 + v2| v3 = -v1 -v2) (it's a value that we're looking for)
7. If complement in seen and seen[complement] == i -> add to result sorted tuple of val1, val2 and complement
8. add to dict val2 -> index of val1
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for val2 in nums[i+1:]:
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res



if __name__ == '__main__':
    n = ...
    sol = Solution()
    res = sol.func(n)
    print(f'Result --> {res}')  