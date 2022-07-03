"""
Status -> Implemented with solution


"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefixsum = [nums[0]]
        for ind, num in enumerate(nums[1:], 1):
            prefixsum.append(num + prefixsum[ind -1])
        print(prefixsum)

        pass

class BestSolution:
    '''
    Time complexity -> O(N)
    Space complexity -> O(1)

    Solution
    1. initiate current and max counter
    2. iterate over nums
    3. put in counter max of num or current counter + num (if current counter less plus num is less then num it means that we start from num)
    4. keep max counter updated to current counter
    '''
    def maxSubArray(self, nums: list[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray



if __name__ == '__main__':
    n = [-2,1,-3,4,-1,2,1,-5,4]
    n = [0, -1, 1, 2, 3, -3, 2]
    # n = [-1, -1, 100, -1, -7, 1, 1000]
    sol = BestSolution()
    res = sol.maxSubArray(n)
    print(f'Result --> {res}')  