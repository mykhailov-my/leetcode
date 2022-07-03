"""
Status -> (Solved by myself, Solved with hint, Solved on review, Implemented with solution)

Time complexity -> O(N)
Space complexity -> O(1)

Solution
1. sum counter = 0; sum_max = -inf
2. iterate over nums
3. if we summed up k and more elements -> get max sum (Don;t do it before first k sum formed)
4. if we moving more then k -> subtract begin of nums (nums[ind - k])
5. return max / k
"""


class Solution:

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = 0
        max_sum = float('-inf')
        for ind, num in enumerate(nums):
            current_sum += num
            if ind >= k:
                current_sum -= nums[ind - k]
            if ind + 1 >= k:
                max_sum = max(max_sum, current_sum)

        return max_sum / k


if __name__ == '__main__':
    n = [1, 12, -5, -6, 50, 3]
    k = 4
    n = [-1]
    k = 1
    n = [
        -6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284,
        -3024, 1714, -2825, -2374, -2750, -959, 6516, 9356, 8040, -2169, -9490,
        -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337,
        -9158, -4183, 6240, -2846, -2588, -5458, -9576, -1501, -908, -5477,
        7596, -8863, -4088, 7922, 8231, -4928, 7636, -3994, -243, -1327, 8425,
        -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831,
        2854, -4498, -6983, -677, 2216, -1938, 3348, 4099, 3591, 9076, 942,
        4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296,
        -3280, 8909, -8352, -9413, 3513, 1352, -8825
    ]
    k = 90
    # n = [9,7,3,5,6,2,0,8,1,9]
    # k = 6
    # n = [1,12,-5,-6,50,3]
    # k = 4

    sol = Solution()
    res = sol.findMaxAverage(n, k)
    print(f'Result --> {res}')
