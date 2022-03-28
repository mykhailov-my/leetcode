class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])

        """
        Do not return anything, modify nums in-place instead.
        """

if __name__ == '__main__':
    nums = [1,2]
    key = 3
    sol = Solution()
    # breakpoint()
    # print(id(nums))
    res = sol.rotate(nums, key)
    print(f'Result --> {nums}')
