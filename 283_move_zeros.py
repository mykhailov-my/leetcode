class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_substract = 0
        for idx, num in enumerate(nums):
            if nums[idx - idx_substract] == 0:
                nums.append(nums.pop(idx - idx_substract))
                idx_substract += 1

if __name__ == '__main__':
    n = [0,0,1,0,3,12]
    sol = Solution()
    res = sol.moveZeroes(n)
    print(f'Result --> {n}')