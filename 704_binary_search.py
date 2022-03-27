
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def recursive_search(nums: list[int], target, start_idx = 0) -> int:
            if len(nums) == 1:
                if nums[0] == target:
                    return start_idx
                else:
                    return None
            else:
                first_half = nums[:round(len(nums) / 2)]
                if first_half[-1] >= target:
                    return recursive_search(first_half, target, start_idx = start_idx)
                else:
                    second_half = nums[round(len(nums) / 2):]
                    return recursive_search(second_half, target, start_idx = start_idx + round(len(nums) / 2))
        result = recursive_search(nums, target)
        return result if result is not None else -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = Solution()
    res = sol.search(nums, target)
    print(f'Result --> {res}')
    