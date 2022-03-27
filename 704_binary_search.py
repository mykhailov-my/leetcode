
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def recursive_search(nums: list[int], target, start_idx = 0) -> int:
            if len(nums) == 1:
                if nums[0] == target:
                    return start_idx
                else:
                    return None
            else:
                first_half = recursive_search(nums[:round(len(nums) / 2)], target, start_idx = start_idx)
                second_half = recursive_search(nums[round(len(nums) / 2):], target, start_idx = start_idx + round(len(nums) / 2))
                if first_half is not None:
                    return first_half
                else:
                    return second_half
        result = recursive_search(nums, target)
        return result if result is not None else -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    nums = [2,5]
    target = 2
    sol = Solution()
    res = sol.search(nums, target)
    print(f'Result --> {res}')
    