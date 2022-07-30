"""
Status -> Solved by myself

__init__
Time complexity -> O(N)
Space complexity -> O(N)

pickIndex
Time complexity -> O(log N)
Space complexity -> O(1)

Solution
1. init -> save prefix sum of list

pickIndex
2. get random float from 0 to last el of PS
3. use bi search to find a place for rnd in PS list
4. return it's index
"""

from bisect import bisect_left
from collections import Counter
from random import uniform


class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sum = [w[0]]
        for num in w[1:]:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def pickIndex(self) -> int:
        rnd = uniform(0, self.prefix_sum[-1])
        ind = bisect_left(self.prefix_sum, rnd)
        return ind


if __name__ == '__main__':

    sol = Solution([1,3,1,5])
    res = Counter([sol.pickIndex() for i in range(1000)])
    # res = sol.pickIndex()
    print(f'Result --> {res}')  