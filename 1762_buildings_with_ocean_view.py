"""
Status -> Solved by myself

Time complexity -> O(N)
Space complexity -> O(N)

Solution
1. go from right to left
2. max = 0; if el > max -> add to begin of queue index, max = el
3. return queue
"""
from collections import deque

class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        result = deque()
        end = len(heights) - 1
        max_val = 0
        while end >= 0:
            if heights[end] > max_val:
                result.appendleft(end)
                max_val = heights[end]
            end -= 1
        return result



if __name__ == '__main__':
    n = [1,3,2,4]
    sol = Solution()
    res = sol.findBuildings(n)
    print(f'Result --> {res}')  