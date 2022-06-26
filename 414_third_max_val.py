"""
Status -> Implemented with solution

Time complexity -> O(N)
Space complexity -> O(1)

Solution
1. add all numbers to set
2. if there is more then 3 remove min of them
3. if total len less 3 - return max else min
"""

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

if __name__ == '__main__':
    # n = [2,0,1, -3]
    n = [1, 2, 2, 2, 2, 2, 3, 2, 3, 1]
    sol = Solution()
    res = sol.thirdMax(n)
    print(f'Result --> {res}')