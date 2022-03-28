
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def recursive_search(nums: list[int], target, start_idx = 0) -> int:
            if len(nums) == 1:
                if nums[0] == target:
                    return start_idx
                elif nums[0] < target:
                    return start_idx + 1
                elif start_idx == 0 and nums[0] > target:
                    return 0
                else:
                    return None
            else:
                first_half = nums[:round(len(nums) / 2)]
                second_half = nums[round(len(nums) / 2):]
                if first_half[-1] < target and target < second_half[0]:
                    return round(len(nums) / 2) + start_idx
                elif first_half[-1] >= target:
                    return recursive_search(first_half, target, start_idx = start_idx)
                else:
                    return recursive_search(second_half, target, start_idx = start_idx + round(len(nums) / 2))
        return recursive_search(nums, target)

if __name__ == '__main__':
    nums = [3,5,7,9,10]
    target = 8
    sol = Solution()
    res = sol.searchInsert(nums, target)
    print(f'Result --> {res}')
    