class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # quick sort once, pivot is 1
        left = 0
        right = len(nums) - 1
        pivot = nums[int(len(nums) / 2)]
        while left < right:
            while nums[left] < pivot and left < len(nums) - 1:
                left += 1
            while nums[right] > pivot and right > 0:
                right -= 1
            breakpoint()
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] == nums[right]:
                break

        return nums
        
if __name__ == '__main__':
    n = [2,0,1] #[1, 0, 2]
    # n = [2,0,2,1,1,0]
    # n = [1, 0, 1]
    # [2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    sol = Solution()
    res = sol.sortColors(n)
    print(f'Result --> {res}')