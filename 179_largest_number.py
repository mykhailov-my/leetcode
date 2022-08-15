"""
Status -> Solved with hint

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. Quicksort by custom comparison 
2. compare by converting two ints to string, concat and convert to int again. compare them
3. build a string out of list of nums
4. if first symbol is 0 - return 0 else string
"""
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(x, y):
            if int(f'{x}{y}') > int(f'{y}{x}'):
                return 1
            elif int(f'{x}{y}') < int(f'{y}{x}'):
                return -1 
            else:
                return 0

        nums.sort(key=cmp_to_key(cmp), reverse=True)
        res = ''.join(map(str, nums))
        return '0' if res[0] == '0' else res



if __name__ == '__main__':
    n = [3,30,34,5,9] # 9 5 34 3 30
    n = [1, 61, 6, 67] # 67 6 61 1
    # n = [70, 7]
    n = [0, 0]
    sol = Solution()
    res = sol.largestNumber(n)
    print(f'Result --> {res}')  