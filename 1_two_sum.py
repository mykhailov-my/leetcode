
class Solution:
    """
    Status -> Solved by mysel

    Tags -> Hash

    Time complexity -> O(N)
    Space complexity -> O(N)

    Solution
    1. Init dict
    2. Iterate by nums
    3. if target - current num in map -> return current index and index from map
    4. else add to map num-> index

    Notes 
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return i, nums_map[target - nums[i]]
            else:
                nums_map[nums[i]] = i



if __name__ == '__main__':
    n = [2,7,11,15]
    t = 9
    n = [3,3]
    t = 6
    sol = Solution()
    res = sol.twoSum(n, t)
    print(f'Result --> {res}')  