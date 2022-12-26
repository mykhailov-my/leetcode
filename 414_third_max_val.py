"""
Status -> Implemented with solution

Time complexity -> O(N)
Space complexity -> O(1)

Solution
1. add all numbers to set
2. if there is more then 3 remove min of them
3. if total len less 3 - return max else min
"""

import heapq


class WorstSolution:
    #Time complexity O(N + N log N)
    #Space complexity
    def thirdMax(self, nums):
        l = sorted(list(set(nums)), reverse=True)
        if len(l) < 3:
            return max(l)
        return l[2]


class BestSolution:
    def thirdMax(self, nums: list[int]) -> int:
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)


class Solution2:
    """
    Status -> Resolved by myself

    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. convert to set nums
    2. if set less 3 -> return max of set
    3. else ->
        3.1 create heap
        3.2 iterate over heap, add nums to itt keeping fixed size
        3.3 return n largest from heap
    
    LC best perfomance
    time -> 98%
    memory -> 52%
    """
    def thirdMax(self, nums: list[int]) -> int:
        s = set(nums)
        if len(s) < 3:
            return max(s)
        else:
            heap = []
            for n in s:
                if len(heap) < 3:
                    heapq.heappush(heap, n)
                else:
                    heapq.heappushpop(heap, n)
            return heapq.nlargest(3, heap)





if __name__ == '__main__':
    # n = [2,0,1, -3]
    n = [1, 2, 2, 2, 2, 2, 3, 2, 3, 1]
    n = [1,2,2,3,4]
    sol = Solution2()
    res = sol.thirdMax(n)
    print(f'Result --> {res}')