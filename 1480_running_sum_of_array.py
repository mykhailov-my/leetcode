class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_ = 0
        for ind in range(len(nums)):
            sum_ += nums[ind]
            nums[ind] = sum_
        return nums