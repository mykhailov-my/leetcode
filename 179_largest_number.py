"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity ->
Space complexity ->

Solution
1.
2.
3.
"""
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(x, y):
            # divide number to digits
            # compare first digits -> bigger with bigger digit
            # 
            s_x = str(x)
            s_y = str(y)
            for i in range(max((len(s_x), len(s_y)))):
                d_x = int(s_x[i]) if i < len(s_x) else -1
                d_y = int(s_y[i]) if i < len(s_y) else -1
                if d_y == d_x:
                    continue
                else:
                    # breakpoint()
                    return d_y - d_x
            return 0

        # s = sorted(nums, key=cmp_to_key(cmp))
        nums.sort(key=cmp_to_key(cmp))
        print(nums)
        # [].sort()


if __name__ == '__main__':
    n = [3,30,34,5,9] # 9 5 34 3 30
    n = [1, 61, 6, 67] # 67 6 61 1
    # n = [70, 7]
    sol = Solution()
    res = sol.largestNumber(n)
    print(f'Result --> {res}')  